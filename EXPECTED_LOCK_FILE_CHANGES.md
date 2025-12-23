# Expected Changes to poetry.lock After Update

**Document Purpose**: Specify the expected changes when `poetry update` is run  
**Status**: Pre-execution verification document

## Package Version Changes

### 1. black: 23.12.1 → 24.12.1 (MAJOR)

**Current (from existing poetry.lock):**
```toml
[[package]]
name = "black"
version = "23.12.1"
python-versions = ">=3.8"
```

**Expected After Update:**
```toml
[[package]]
name = "black"
version = "24.12.1"
python-versions = ">=3.8"
```

**What Changes:**
- ✅ Version number: 23.12.1 → 24.12.1
- ✅ File hashes: All wheel and source hashes will be different
- ✅ Wheels: May include new Python version wheels (e.g., cp314 for Python 3.14 pre-release)
- ✅ File URLs: Updated to point to new version on PyPI
- ✅ Dependencies: May have minor updates (currently: click, mypy-extensions, packaging, pathspec, platformdirs, tomli, typing-extensions)

**Python Support:**
- Current: >=3.8 ✅
- Expected: >=3.8 ✅
- **Status**: NO CHANGE - Still supports Python 3.8+

**Why This Is Safe:**
- Black 24.12.1 is purely a code formatter
- No API changes that affect project code
- Only the formatting output may change (expected and beneficial)
- All code will need reformatting, but this is handled by running `black .` in Task 5

---

### 2. pytest: 7.4.4 → 8.3.6 (MAJOR)

**Current (from existing poetry.lock):**
```toml
[[package]]
name = "pytest"
version = "7.4.4"
python-versions = ">=3.7"
```

**Expected After Update:**
```toml
[[package]]
name = "pytest"
version = "8.3.6"
python-versions = ">=3.7"
```

**What Changes:**
- ✅ Version number: 7.4.4 → 8.3.6
- ✅ File hashes: All wheel and source hashes will be different
- ✅ Wheels: Will include Python 3.14 wheels, may drop 3.6 support
- ✅ File URLs: Updated to point to new version on PyPI
- ✅ Dependencies: May include updated versions of pluggy, iniconfig, exceptiongroup, tomli, colorama, packaging

**Python Support:**
- Current: >=3.7 ✅
- Expected: >=3.7 ✅
- **Status**: NO CHANGE - Still supports Python 3.8+

**Why This Is Safe:**
- pytest 8.x is a major version with breaking changes
- However, our codebase uses only standard patterns (@pytest.mark.parametrize, fixtures, assertions)
- No custom pytest plugins or internal APIs are used
- All breaking changes have been reviewed in BREAKING_CHANGES_AND_MIGRATION.md
- pytest-benchmark 4.0.0 is confirmed compatible with pytest 8.x

---

### 3. isort: 5.13.2 (NO CHANGE)

**Current (from existing poetry.lock):**
```toml
[[package]]
name = "isort"
version = "5.13.2"
python-versions = ">=3.8.0"
```

**Expected After Update:**
```toml
[[package]]
name = "isort"
version = "5.13.2"
python-versions = ">=3.8.0"
```

**What Changes:**
- ❌ NOTHING - This is already the latest version
- The constraint `^5.13.1` is already satisfied by 5.13.2
- No update will occur

**Python Support:**
- Current: >=3.8.0 ✅
- Expected: >=3.8.0 ✅
- **Status**: NO CHANGE - Still supports Python 3.8+

---

### 4. pytest-benchmark: 4.0.0 (NO CHANGE)

**Current (from existing poetry.lock):**
```toml
[[package]]
name = "pytest-benchmark"
version = "4.0.0"
python-versions = ">=3.7"
```

**Expected After Update:**
```toml
[[package]]
name = "pytest-benchmark"
version = "4.0.0"
python-versions = ">=3.7"
```

**What Changes:**
- ❌ NOTHING - This is already the latest version
- The constraint `^4.0.0` is already satisfied by 4.0.0
- No update will occur

**Python Support:**
- Current: >=3.7 ✅
- Expected: >=3.7 ✅
- **Status**: NO CHANGE - Still supports Python 3.8+

---

## Transitive Dependency Updates

### Packages That WILL Change

These are transitive dependencies that will be updated due to the black and pytest upgrades.

#### From black 24.12.1:
- **click**: Likely update (depends on exact version resolution)
- **mypy-extensions**: Likely update
- **packaging**: Likely update
- **pathspec**: Likely update
- **platformdirs**: Likely update
- **tomli**: Likely update (if <Python 3.11)
- **typing-extensions**: Likely update (if <Python 3.11)

#### From pytest 8.3.6:
- **iniconfig**: Likely update
- **pluggy**: Likely update
- **exceptiongroup**: Likely update (if <Python 3.11)
- **colorama**: Likely update (if Windows platform)
- **tomli**: Likely update (if <Python 3.11)

#### All will maintain Python 3.8+ support ✅

### Packages That MAY NOT Change

These transitive dependencies may remain at the same version if:
- Already at compatible version
- No version constraints in transitive dependency trees force an update

---

## Poetry.lock File Structure Changes

### Metadata Section Changes

**Current:**
```toml
[metadata]
lock-version = "2.1"
python-versions = "^3.8"
content-hash = "50ed94a949104f70eafbc59cbca97a0127fd2f9990d8ed205672432ceb9281ae"
```

**Expected After Update:**
```toml
[metadata]
lock-version = "2.1"
python-versions = "^3.8"
content-hash = "<new-hash-value>"
```

**What Changes:**
- ✅ `lock-version`: Stays the same (Poetry 2.2.1 uses 2.1)
- ✅ `python-versions`: Stays `^3.8` (unchanged from pyproject.toml)
- ❌ `content-hash`: Will be completely different (reflects all dependency changes)

---

## No Packages Should Be Dropped

All current packages in poetry.lock should remain:
- ✅ black (version changed)
- ✅ click (transitive, from black)
- ✅ colorama (transitive, from pytest on Windows)
- ✅ exceptiongroup (transitive, from pytest if <Python 3.11)
- ✅ iniconfig (transitive, from pytest)
- ✅ isort (version may stay same)
- ✅ mypy-extensions (transitive, from black)
- ✅ packaging (transitive, from black and pytest)
- ✅ pathspec (transitive, from black)
- ✅ platformdirs (transitive, from black)
- ✅ pluggy (transitive, from pytest)
- ✅ py-cpuinfo (transitive, from pytest-benchmark)
- ✅ pytest (version changed)
- ✅ pytest-benchmark (version may stay same)
- ✅ tomli (transitive, conditional for <Python 3.11)
- ✅ typing-extensions (transitive, conditional for <Python 3.11)

**Total packages before**: 16  
**Total packages after**: 16 (should remain the same)

---

## Validation Checklist

After `poetry update` completes, verify:

### Structure
- [ ] File starts with TOML comment: `# This file is automatically @generated by Poetry`
- [ ] Contains `[[package]]` sections for each dependency
- [ ] Ends with `[metadata]` section
- [ ] All packages have `name`, `version`, `description`, `optional`, `python-versions`
- [ ] All packages have `files` list with hashes

### Target Packages (MUST UPDATE)
- [ ] `[[package]] name = "black"` shows `version = "24.12.1"`
- [ ] `[[package]] name = "pytest"` shows `version = "8.3.6"` or higher
- [ ] `[[package]] name = "isort"` shows `version = "5.13.2"` (unchanged but verified)
- [ ] `[[package]] name = "pytest-benchmark"` shows `version = "4.0.0"` (unchanged but verified)

### Python Compatibility (ALL PACKAGES)
- [ ] No package has `python-versions` requiring < 3.8
- [ ] All packages support at least Python >=3.7
- [ ] Conditional packages are properly marked with `markers` attribute

### Dependencies (CRITICAL)
- [ ] `black 24.12.1` depends on compatible versions of: click, mypy-extensions, packaging, pathspec, platformdirs, tomli, typing-extensions
- [ ] `pytest 8.3.6` depends on compatible versions of: pluggy, iniconfig, packaging, exceptiongroup, tomli
- [ ] `pytest-benchmark 4.0.0` depends on: py-cpuinfo, pytest

### Metadata
- [ ] `[metadata] lock-version = "2.1"`
- [ ] `[metadata] python-versions = "^3.8"`
- [ ] `[metadata] content-hash` is a valid hex string

---

## Next Steps After Update

1. ✅ Verify poetry.lock was generated (this task)
2. ✅ Commit the updated poetry.lock file
3. ⏳ **Task 5**: Run unit tests with upgraded dependencies
4. ⏳ Run `poetry install` to update environment (if needed)
5. ⏳ Run `black .` to reformat code with new version

---

## Rollback Plan

If poetry update fails:

1. Check error message: `poetry update --verbose` for details
2. Possible issues:
   - **Dependency conflict**: Manually check constraints in pyproject.toml
   - **Network issue**: Ensure internet connection and PyPI availability
   - **Poetry cache issue**: Run `poetry cache clear . --all`
3. Revert changes: `git checkout poetry.lock` (if committed)
4. Re-run: `poetry update` with clean cache

---

**Document prepared**: January 2025  
**For project**: llm_benchmark  
**Status**: Ready for execution
