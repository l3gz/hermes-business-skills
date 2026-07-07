#!/usr/bin/env bash
#
# install.sh — One-liner installer for Hermes Business Skills
#
# Installs marketing skills directly into ~/.hermes/skills/ (or a profile-specific
# skills directory). No clone folder left behind.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash
#
#   # Install a specific pack:
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash -s -- --pack marketing-agent
#
#   # Install all skills:
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash -s -- --all
#
#   # Install into a specific profile:
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash -s -- --profile matt
#
#   # Install into a custom target directory:
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash -s -- --target ~/my-skills
#
#   # Dry run (show what would be installed without copying):
#   curl -fsSL https://raw.githubusercontent.com/l3gz/hermes-business-skills/master/install.sh | bash -s -- --dry-run
#
set -euo pipefail

REPO="l3gz/hermes-business-skills"
BRANCH="master"
TMPDIR_BASE="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_BASE"' EXIT

echo "Cloning $REPO to temporary directory..."
git clone --quiet --depth 1 --branch "$BRANCH" "https://github.com/$REPO.git" "$TMPDIR_BASE/repo" 2>/dev/null || {
    echo "Error: failed to clone $REPO" >&2
    exit 1
}

echo "Running installer..."
echo ""

# Forward all args to the Python installer
if [ $# -eq 0 ]; then
    # Default: install the full marketing pack
    python3 "$TMPDIR_BASE/repo/scripts/install_skills.py" --pack marketing
else
    python3 "$TMPDIR_BASE/repo/scripts/install_skills.py" "$@"
fi

# Temp clone is cleaned up by the trap on exit
echo ""
echo "Temporary clone removed. Skills are installed directly in your Hermes skills directory."
