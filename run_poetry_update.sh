#!/bin/bash
# Script to update poetry.lock with new dependency versions
# This script runs poetry update to resolve all dependencies

set -e

echo "Starting poetry update with new dependency constraints..."
echo "Target versions:"
echo "  - black: ^24.0 (from ^23.12.0)"
echo "  - pytest: ^8.0 (from ^7.4.3)"
echo "  - isort: ^5.13.1 (maintained)"
echo "  - pytest-benchmark: ^4.0.0 (maintained)"
echo ""

# Run poetry update to resolve dependencies
poetry update

echo ""
echo "Poetry update completed successfully!"
echo "Updated poetry.lock file with new dependency versions."
