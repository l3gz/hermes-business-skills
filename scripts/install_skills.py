#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'

PACKS = {
    'marketing': [
        'avatar-builder',
        'attractive-character-builder',
        'offer-builder',
        'hook-angle-writer',
        'brand-voice-extractor',
        'podcast-to-copy',
        'nurture-email-writer',
        'launch-email-writer',
        'funnel-page-writer',
        'human-editor',
    ],
}


def default_target() -> Path:
    home = os.environ.get('HERMES_HOME')
    if home:
        return Path(home).expanduser() / 'skills'
    return Path.home() / '.hermes' / 'skills'


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
    parser.add_argument('--pack', choices=sorted(PACKS), action='append', help='Install a named pack')
    parser.add_argument('--skill', action='append', help='Install a single skill')
    parser.add_argument('--all', action='store_true', help='Install all available skills')
    parser.add_argument('--target', default=str(default_target()), help='Target Hermes skills directory')
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

    target = Path(args.target).expanduser().resolve()
    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    print(f'Target: {target}')
    for name in selected:
        copy_skill(name, target, args.dry_run)
    print('Done. Restart Hermes or run /reset so installed skills are visible.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
