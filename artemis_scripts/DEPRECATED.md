# ⚠️ DEPRECATED: artemis_scripts Folder

This folder and all scripts within it are **deprecated** as of the latest release.

## What Happened?

The functionality previously provided by these shell scripts has been replaced by a modern `Makefile` with simple, memorable commands. The Makefile approach provides:

- **Simpler commands** - `make install` instead of `bash artemis_scripts/build.sh`
- **Better documentation** - Run `make help` to see all available commands
- **Consistency** - All workflows use the same Makefile infrastructure
- **Maintainability** - Single source of truth for build commands

## Migration Guide

If you're currently using these scripts, migrate to the following `make` commands:

| Old Script | New Command | Purpose |
|-----------|------------|---------|
| `bash artemis_scripts/build.sh` | `make install` or `make build` | Install project dependencies |
| `bash artemis_scripts/test.sh` | `make test` | Run unit tests (without benchmarks) |
| `bash artemis_scripts/benchmark.sh` | `make benchmark` | Run performance benchmarks |
| `bash artemis_scripts/clean.sh` | `make clean` | Remove cache and build artifacts |

## Quick Start with New Commands

```bash
# Install dependencies
make install

# Run tests
make test

# Run benchmarks
make benchmark

# Clean artifacts
make clean

# See all available commands
make help
```

## Why Are These Scripts Still Here?

These scripts are kept for **backward compatibility** during the transition period. They still function and will execute the Poetry commands as before, but they now display deprecation warnings.

## Timeline for Removal

- **Current Version:** Scripts present with deprecation notices
- **Future Version:** These scripts will be removed entirely
- **Recommendation:** Update your workflows to use `make` commands before the next major release

## Need Help?

- See the main [README.md](../README.md) for the full "Development Commands" section
- Run `make help` to see all available commands with descriptions
- Each `make` command shows exactly what it's executing

---

**Status:** These scripts are deprecated and scheduled for removal. Please migrate to `make` commands.

