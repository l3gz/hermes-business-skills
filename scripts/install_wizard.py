#!/usr/bin/env python3
"""Guided wizard for installing Hermes business skills.

Wraps install_skills.py with either an interactive prompt flow or
a non-interactive --yes flow that just forwards CLI flags.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTALL = HERE / 'install_skills.py'


def ask(prompt: str, default: str | None = None) -> str:
    suffix = f' [{default}]' if default else ''
    value = input(f'{prompt}{suffix}: ').strip()
    return value or (default or '')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Guided wizard for installing Hermes business skills.',
    )
    parser.add_argument('--pack', action='append', help='Install a named pack (repeatable)')
    parser.add_argument('--skill', action='append', help='Install a single skill by name (repeatable)')
    parser.add_argument('--all', action='store_true', help='Install every skill in this repo')
    parser.add_argument(
        '--target',
        default=None,
        help='Target Hermes skills directory. Defaults to the active profile when HERMES_PROFILE is set.',
    )
    parser.add_argument('--dry-run', action='store_true', help='Print actions without copying')
    parser.add_argument(
        '--yes',
        action='store_true',
        help='Run non-interactively using the provided flags (or sensible defaults).',
    )
    return parser.parse_args()


def build_command(args: argparse.Namespace) -> list[str]:
    cmd = [sys.executable, str(INSTALL)]
    if args.all:
        cmd.append('--all')
    for pack in args.pack or []:
        cmd.extend(['--pack', pack])
    for skill in args.skill or []:
        cmd.extend(['--skill', skill])
    if args.target:
        cmd.extend(['--target', args.target])
    if args.dry_run:
        cmd.append('--dry-run')
    return cmd


def main() -> int:
    args = parse_args()

    has_flags = bool(args.pack or args.skill or args.all or args.target)
    if args.yes and not has_flags:
        # --yes without flags = default to installing the marketing pack.
        args.pack = ['marketing']

    if not args.yes:
        if not has_flags:
            print('Hermes Business Skills Wizard')
            print('-----------------------------')
            print('Available packs: marketing')
            raw = ask('Packs to install, comma-separated', 'marketing')
            args.pack = [p.strip() for p in raw.split(',') if p.strip()] or ['marketing']
            skill_raw = ask('Single skills to install, comma-separated (blank for none)', '')
            if skill_raw.strip():
                args.skill = [s.strip() for s in skill_raw.split(',') if s.strip()]
            args.dry_run = ask('Dry run first? yes/no', 'yes').lower() in {'y', 'yes'}
            target_raw = ask('Target skills directory, blank for default', '')
            if target_raw.strip():
                args.target = target_raw.strip()

    cmd = build_command(args)
    code = subprocess.call(cmd)
    if args.dry_run and code == 0:
        print('\nDry run complete. Re-run with --dry-run omitted to install.')
    return code


if __name__ == '__main__':
    raise SystemExit(main())