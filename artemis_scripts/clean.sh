#!/bin/bash
#
# ⚠️ DEPRECATED: This script is deprecated as of the latest release.
# Functionality has been replaced by the Makefile.
#
# MIGRATION: Use `make clean` instead
# For more information, see artemis_scripts/DEPRECATED.md
#

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Expect CLEAN to be defined in variables.sh
echo "Running clean command: $CLEAN"
if [ -z "${CLEAN:-}" ]; then
  exit 0
fi
eval "$CLEAN"