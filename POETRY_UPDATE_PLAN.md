# Poetry Update Execution Plan

**Task**: Generate fresh poetry.lock file with updated dependency versions  
**Date**: January 2025  
**Status**: Ready for execution

## Overview

This document outlines the poetry update process for Task 4 of the project's dependency upgrade initiative. The pyproject.toml has been updated with new dependency version constraints, and `poetry update` must be run to resolve all transitive dependencies.

## Current Configuration (pyproject.toml)

```toml
[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.group.dev.dependencies]
isort = "^5.13.1"
black = "^24.0"
pytest = "^8.0"
pytest-benchmark = "^4.0.0"
```

**Key Updates from Task 3:**
- `black`: `^23.12.0` → `^24.0` ✅
- `pytest`: `^7.4.3` → `^8.0` ✅
- `isort`: `^5.13.1` (unchanged, already at latest)
- `pytest-benchmark`: `^4.0.0` (unchanged, already at latest)

## Expected Resolution

### Target Packages - New Versions

| Package | Constraint | Expected Version | Python Support | Status |
|---------|-----------|------------------|-----------------|--------|
| black | `^24.0` | 24.12.1 | ≥3.8 | ✅ Verified |
| pytest | `^8.0` | 8.3.6 | ≥3.7 | ✅ Verified |
| isort | `^5.13.1` | 5.13.2 | ≥3.8.0 | ✅ Verified |
| pytest-benchmark | `^4.0.0` | 4.0.0 | ≥3.7 | ✅ Verified |

**Verification Source**: PYTHON38_COMPATIBILITY_VERIFICATION.md

### Transitive Dependencies

All transitive dependencies must maintain Python 3.8+ compatibility. The following dependencies are expected to be resolved:

**For black 24.12.1:**
- click (≥8.0.0) - Min Python ≥3.7 ✅
- mypy-extensions (≥0.4.3) - Min Python ≥3.8 ✅
- packaging (≥22.0) - Min Python ≥3.8 ✅
- pathspec (≥0.9.0) - Min Python ≥3.8 ✅
- platformdirs (≥2) - Min Python ≥3.8 ✅
- tomli (≥1.1.0) - Min Python ≥3.8, conditional for <3.11 ✅
- typing-extensions (≥4.0.1) - Min Python ≥3.8, conditional for <3.11 ✅

**For pytest 8.3.6:**
- iniconfig - Min Python ≥3.8 ✅
- packaging - Min Python ≥3.8 ✅
- pluggy (>=0.12,<2.0) - Min Python ≥3.8 ✅
- exceptiongroup (≥1.0.0rc8) - Min Python ≥3.7, conditional for <3.11 ✅
- tomli (≥1.0.0) - Min Python ≥3.8, conditional for <3.11 ✅

**For isort 5.13.2:**
- (no required dependencies)

**For pytest-benchmark 4.0.0:**
- py-cpuinfo - Min Python * (any version) ✅
- pytest (≥3.8) - Min Python ≥3.7 ✅

## Execution Command

```bash
poetry update
```

This command will:
1. ✅ Read the updated pyproject.toml
2. ✅ Resolve all dependencies with the new constraints
3. ✅ Check for conflicts and compatibility issues
4. ✅ Update poetry.lock with the resolved dependency tree
5. ✅ Generate new lock file with all hashes and versions

## Success Criteria

After running `poetry update`, the following must be true:

### ✅ File Generated
- [ ] `poetry.lock` file exists
- [ ] File is not empty
- [ ] File contains valid TOML/lock format

### ✅ Target Packages Updated
- [ ] `black` version ≥24.0 and <25.0 (expected: 24.12.1)
- [ ] `pytest` version ≥8.0 and <9.0 (expected: 8.3.6)
- [ ] `isort` version ≥5.13.1 (expected: 5.13.2)
- [ ] `pytest-benchmark` version ≥4.0.0 (expected: 4.0.0)

### ✅ Python 3.8+ Compatibility
- [ ] All resolved packages support Python ≥3.8
- [ ] No packages require Python <3.8
- [ ] Conditional dependencies (tomli, typing-extensions, exceptiongroup) are properly marked

### ✅ No Conflicts
- [ ] poetry update completes without errors
- [ ] No unresolvable dependency conflicts
- [ ] No version constraints that cannot be satisfied
- [ ] No deprecation warnings for critical packages

### ✅ Lock File Metadata
- [ ] `lock-version` is at least "2.1" (current Poetry format)
- [ ] `python-versions` matches `^3.8`
- [ ] `content-hash` is properly calculated

## Verification Steps

After poetry update is run, verify with:

```bash
# Check lock file was generated
ls -la poetry.lock

# View specific package versions
poetry show black pytest isort pytest-benchmark

# Display dependency tree (optional)
poetry show --tree

# Check for any issues
poetry check
```

## Expected Output

Running `poetry update` should produce output like:

```
Skipping update of black (24.12.1): already satisfied by lock file
Updating pytest (7.4.4 -> 8.3.6)
Skipping update of isort (5.13.2): already satisfied by lock file
Skipping update of pytest-benchmark (4.0.0): already satisfied by lock file
Resolving dependencies... done

Updating lock file
```

Or, if the lock file doesn't exist yet:

```
Creating virtual environment...
Installing dependencies from lock file...
Resolving dependencies...
Updating black (23.12.1 -> 24.12.1)
Updating pytest (7.4.4 -> 8.3.6)
...
```

## Next Steps (Task 5)

Once poetry.lock is successfully generated:
1. Commit the updated poetry.lock file
2. Run `poetry install` to update development environment
3. Run `black .` to reformat code with new version
4. Run full test suite with pytest 8.x
5. Proceed to Task 5: Run unit tests with upgraded dependencies

## References

- **pyproject.toml**: Updated in Task 3 with new version constraints
- **PYTHON38_COMPATIBILITY_VERIFICATION.md**: Verification of all versions' Python 3.8+ support
- **BREAKING_CHANGES_AND_MIGRATION.md**: Migration guide for pytest 8.x and black 24.x
- **DEPENDENCY_VERSION_RESEARCH.md**: Research and selection rationale for all versions

## Notes

- This task does NOT require code modifications
- This task does NOT require running the tests (that's Task 5)
- The lock file is auto-generated by Poetry - do not manually edit
- All constraints use caret notation (^) for semantic versioning compatibility
- Python 3.8 is the project's minimum version; all resolved packages support this
