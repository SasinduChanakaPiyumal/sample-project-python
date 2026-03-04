#!/bin/bash
#
# ⚠️ DEPRECATED: This script is deprecated as of the latest release.
# Functionality has been replaced by the Makefile.
#
# MIGRATION: Use `make benchmark` instead
# For more information, see artemis_scripts/DEPRECATED.md
#

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate BENCHMARK with the benchmark command
BENCHMARK="poetry run pytest --benchmark-only tests/"
echo "Running benchmark command: $BENCHMARK"
eval $BENCHMARK
