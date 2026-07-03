#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'
MANIFEST = ROOT / 'manifest.yaml'


def real_home() -> Path:
    """Return the actual user home, ignoring Hermes's per-profile HOME sandbox.

    Hermes sets HOME to ``~/.hermes/profiles/<name>/home`` during sessions, which
    breaks any ``Path('~').expanduser()`` or ``Path.home()`` call. We unwrap that
    pattern by dropping ``.hermes/profiles/<name>/home`` so unrelated HOME
    overrides (and unrelated ``.hermes`` directories higher up) still work.
    """
    home = Path(os.environ.get('HOME', '') or '~').expanduser()
    parts = home.parts
    if 'profiles' in parts and 'home' in parts:
        idx = parts.index('profiles')
        if len(parts) >= idx + 3 and parts[idx + 2] == 'home' and parts[idx + 1]:
            # Drop ``.hermes/profiles/<name>/home`` if .hermes is right before profiles.
            drop_until = idx
            if drop_until >= 1 and parts[drop_until - 1] == '.hermes':
                drop_until -= 1
            return Path(*parts[:drop_until])
    return home


DEFAULT_PROFILE_PATH = real_home() / '.hermes' / 'skills'


def load_packs() -> dict[str, list[str]]:
    if not MANIFEST.exists():
        raise SystemExit(f'Manifest not found: {MANIFEST}')
    if yaml is None:
        raise SystemExit('PyYAML is required to read manifest.yaml. Install with: pip install pyyaml')
    data = yaml.safe_load(MANIFEST.read_text(encoding='utf-8')) or {}
    packs = data.get('packs') or {}
    if not isinstance(packs, dict) or not packs:
        raise SystemExit(f'No packs declared in {MANIFEST}')
    normalized: dict[str, list[str]] = {}
    for name, body in packs.items():
        if not isinstance(body, dict):
            raise SystemExit(f'Pack {name!r} in manifest.yaml must be a mapping with a "skills" list')
        skills = body.get('skills') or []
        if not isinstance(skills, list) or not skills:
            raise SystemExit(f'Pack {name!r} in manifest.yaml has no skills')
        normalized[name] = list(skills)
    return normalized


PACKS: dict[str, list[str]] = load_packs()


def default_target() -> Path:
    """Resolve the install target with profile awareness.

    Order of precedence:
    1. Active Hermes profile (HERMES_PROFILE or HERMES_HOME) → ~/.hermes/profiles/<name>/skills
    2. Explicit HERMES_HOME/skills (when set without HERMES_PROFILE)
    3. ~/.hermes/skills (the shared default profile)
    """
    profile = os.environ.get('HERMES_PROFILE', '').strip()
    hermes_home = os.environ.get('HERMES_HOME', '').strip()

    if profile:
        # Prefer deriving the root from HERMES_HOME so we ignore any per-profile
        # HOME sandboxing (Hermes sets HOME to ~/.hermes/profiles/<name>/home
        # during sessions, which would otherwise double-up the path).
        if hermes_home:
            hermes_root = Path(hermes_home).expanduser().resolve().parent.parent
            return hermes_root / 'profiles' / profile / 'skills'
        return real_home() / '.hermes' / 'profiles' / profile / 'skills'

    if hermes_home:
        return Path(hermes_home).expanduser() / 'skills'

    return DEFAULT_PROFILE_PATH


def resolve_target(arg_target: str | None) -> Path:
    """Pick the install target and emit a cross-profile warning if needed.

    The classic silent-failure case is a user running the installer from inside
    a Hermes session: HOME is sandboxed, HERMES_PROFILE is set, but they unset
    it for the call. We detect that by checking whether HOME is sandboxed without
    HERMES_PROFILE being set, or whether the cwd / script lives under
    ``~/.hermes/profiles/<name>/`` while the resolved target is the default
    profile. Either condition emits a stderr warning.
    """
    if arg_target:
        return Path(arg_target).expanduser().resolve()

    resolved = default_target().expanduser().resolve()
    active_profile = os.environ.get('HERMES_PROFILE', '').strip()

    # Already targeting an explicit profile — nothing to warn about.
    if active_profile and active_profile != 'default':
        return resolved

    default_skills = (real_home() / '.hermes' / 'skills').resolve()
    if resolved != default_skills:
        return resolved

    # Find a profile name we might be running from.
    nested_profile: str | None = None
    home_sandboxed = False

    raw_home = Path(os.environ.get('HOME', '') or '~').expanduser()
    home_parts = raw_home.parts
    if 'profiles' in home_parts and 'home' in home_parts:
        idx = home_parts.index('profiles')
        if len(home_parts) >= idx + 3 and home_parts[idx + 2] == 'home' and home_parts[idx + 1]:
            nested_profile = home_parts[idx + 1]
            home_sandboxed = True

    if not nested_profile:
        for path in (Path.cwd().resolve(), Path(__file__).resolve()):
            parts = path.parts
            if 'profiles' in parts:
                idx = parts.index('profiles')
                if len(parts) > idx + 1 and parts[idx + 1] and parts[idx + 1] != 'default':
                    nested_profile = parts[idx + 1]
                    break

    if nested_profile:
        if home_sandboxed:
            hint = (
                f' Your HOME looks like it belongs to profile {nested_profile!r}; '
                f'export HERMES_PROFILE={nested_profile}, or pass '
                f'--target ~/.hermes/profiles/{nested_profile}/skills explicitly.'
            )
        else:
            hint = (
                f' Set HERMES_PROFILE={nested_profile} or pass '
                f'--target ~/.hermes/profiles/{nested_profile}/skills explicitly.'
            )
        print(
            f'WARNING: detected profile {nested_profile!r} in your environment but '
            f'HERMES_PROFILE is not set, so the install target resolves to the shared '
            f'default profile ({resolved}).{hint}',
            file=sys.stderr,
        )
    return resolved


def all_skill_names() -> list[str]:
    return sorted(p.name for p in SKILLS_DIR.iterdir() if p.is_dir())


def copy_skill(name: str, target: Path, dry_run: bool) -> None:
    src = SKILLS_DIR / name
    if not src.exists():
        raise SystemExit(f'Unknown skill: {name}')
    dst = target / name
    if dry_run:
        print(f'Would install {name} -> {dst}')
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f'Installed {name} -> {dst}')


def main() -> int:
    parser = argparse.ArgumentParser(description='Install Hermes business skills.')
    parser.add_argument('--pack', choices=sorted(PACKS), action='append', help='Install a named pack (repeatable)')
    parser.add_argument('--skill', action='append', help='Install a single skill by name (repeatable)')
    parser.add_argument('--all', action='store_true', help='Install every skill in this repo')
    parser.add_argument(
        '--target',
        default=None,
        help=(
            'Target Hermes skills directory. '
            'Default: ~/.hermes/profiles/<HERMES_PROFILE>/skills when HERMES_PROFILE is set, '
            'otherwise $HERMES_HOME/skills or ~/.hermes/skills.'
        ),
    )
    parser.add_argument('--dry-run', action='store_true', help='Print actions without copying')
    args = parser.parse_args()

    selected: list[str] = []
    if args.all:
        selected.extend(all_skill_names())
    for pack in args.pack or []:
        selected.extend(PACKS[pack])
    for skill in args.skill or []:
        selected.append(skill)

    selected = sorted(dict.fromkeys(selected))
    if not selected:
        parser.error('Choose --all, --pack, or --skill')

    target = resolve_target(args.target)
    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    print(f'Target: {target}')
    for name in selected:
        copy_skill(name, target, args.dry_run)
    print('Done. Restart Hermes or run /reset so installed skills are visible.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())