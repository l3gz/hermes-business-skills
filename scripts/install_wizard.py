#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTALL = HERE / 'install_skills.py'
PACKS = ['marketing']


def ask(prompt: str, default: str | None = None) -> str:
    suffix = f' [{default}]' if default else ''
    value = input(f'{prompt}{suffix}: ').strip()
    return value or (default or '')


def main() -> int:
    print('Hermes Business Skills Wizard')
    print('-----------------------------')
    print('Available packs:')
    for pack in PACKS:
        print(f'- {pack}')
    raw = ask('Packs to install, comma-separated', 'marketing')
    dry = ask('Dry run first? yes/no', 'yes').lower() in {'y', 'yes'}
    target = ask('Target skills directory, blank for default', '')

    cmd = [sys.executable, str(INSTALL)]
    for pack in [p.strip() for p in raw.split(',') if p.strip()]:
        cmd.extend(['--pack', pack])
    if target:
        cmd.extend(['--target', target])
    if dry:
        cmd.append('--dry-run')

    print('\nRunning:', ' '.join(cmd))
    code = subprocess.call(cmd)
    if dry and code == 0:
        print('\nDry run complete. Re-run with dry run = no to install.')
    return code


if __name__ == '__main__':
    raise SystemExit(main())
