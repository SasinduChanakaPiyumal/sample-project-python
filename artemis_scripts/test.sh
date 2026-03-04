#!/bin/bash
#
# ⚠️ DEPRECATED: This script is deprecated as of the latest release.
# Functionality has been replaced by the Makefile.
#
# MIGRATION: Use `make test` instead
# For more information, see artemis_scripts/DEPRECATED.md
#

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate TEST with the test command
TEST="poetry run pytest --benchmark-skip tests/"
echo "Running test command: $TEST"
eval $TEST
