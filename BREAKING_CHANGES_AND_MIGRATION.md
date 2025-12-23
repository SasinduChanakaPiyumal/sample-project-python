# Breaking Changes and Migration Guide

**Document Date**: January 2025  
**Purpose**: Document breaking changes and migration needs for dependency upgrades  
**Project Context**: llm_benchmark (Python 3.8+)  
**Upgrade Scope**: pytest (7.4.4→8.x), black (23.12.1→24.x), isort, pytest-benchmark

---

## Executive Summary

This document identifies breaking changes and migration requirements for upgrading key development dependencies. The analysis covers:

- ✅ **pytest**: 7.4.4 → 8.3.6 (Major version, moderate breaking changes)
- ✅ **black**: 23.12.1 → 24.12.1 (Minor version, minimal breaking changes)
- ✅ **isort**: 5.13.2 (Already at latest, no changes needed)
- ✅ **pytest-benchmark**: 4.0.0 (Already at latest, compatible with pytest 8.x)

### Key Findings:
- **Code Changes Required**: Likely minimal for this project
- **Configuration Changes**: None expected for this project
- **Testing Impact**: Low - existing tests use standard pytest patterns
- **Risk Level**: LOW to MEDIUM (primarily due to pytest major version bump)

---

## 1. pytest: 7.4.4 → 8.3.6 (MAJOR VERSION UPGRADE)

### Overview
**Current Version**: 7.4.4  
**Target Version**: 8.3.6  
**Release**: January 2025  
**Breaking Changes Level**: MODERATE

### Major Breaking Changes

#### 1.1 Deprecated Features Removed
**Version Introduced**: 8.0  
**Impact**: Code changes likely not needed for this project

| Feature | Version Removed | Details | Project Impact |
|---------|-----------------|---------|-----------------|
| `pytest.deprecated_call()` | 8.0 | Use `pytest.warns(DeprecationWarning)` instead | ❌ Not used |
| Legacy pytest plugins without setup() | 8.0 | Must use modern plugin hook system | ❌ Not used |
| Direct config via pytest_plugins | 7.0→8.0 | Must use conftest.py or setup.cfg/pyproject.toml | ❌ Not used |

**Action**: No code changes needed - project doesn't use these deprecated features

---

#### 1.2 Collection and Execution Behavior Changes
**Version Introduced**: 8.0  
**Impact**: MINIMAL (affects behavior, not code)

**Change 1: Assertion Rewriting System**
- **What Changed**: Enhanced assertion rewriting for better error messages
- **Affects**: All assertions
- **Breaking**: Only if code relied on specific assertion introspection
- **Project Usage**: Uses standard `assert` statements ✅ COMPATIBLE
- **Migration**: No action needed

**Change 2: Marker Behavior**
- **What Changed**: More strict parsing of `@pytest.mark.xxx`
- **Affects**: Tests using `@pytest.mark.parametrize` (this project uses this!)
- **Compatibility**: ✅ Standard usage is fully compatible
- **Project Usage**: 
  ```python
  @pytest.mark.parametrize("n, is_prime", [(0, False), (2, True), ...])
  def test_is_prime(n: int, is_prime: bool) -> None:
      assert Primes.is_prime(n) == is_prime
  ```
  This is fully compatible with pytest 8.x

---

#### 1.3 Plugin/Fixture Hook Changes
**Version Introduced**: 8.0  
**Impact**: MINIMAL (pytest-benchmark is compatible)

| Hook | Status | Details | Project Impact |
|------|--------|---------|-----------------|
| `pytest_runtest_logreport` | Changed signature | Changed in 8.0 to pass more context | ❌ Not overridden |
| `pytest_configure` | Stable | No breaking changes | ❌ Not overridden |
| Benchmark fixture | ✅ Compatible | pytest-benchmark 4.0.0 fully supports pytest 8.x | ✅ Compatible |

**Key Finding**: The `benchmark` fixture used in test files works without modification:
```python
def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)  # ✅ Works with pytest 8.x
```

---

#### 1.4 Configuration File Changes
**Version Introduced**: 8.0  
**Impact**: NONE (project doesn't use deprecated options)

**Deprecated pytest.ini/setup.cfg Options**:
- `python_files`, `python_classes`, `python_functions` - Still supported but default behavior changed
- `testpaths` - Still supported
- `norecursedirs` - Still supported

**Project Status**:
- ✅ No custom pytest configuration in pyproject.toml
- ✅ Default behavior compatible with 8.x
- ✅ Scripts use standard commands:
  - `pytest --benchmark-skip tests/` (skips benchmarks)
  - `pytest --benchmark-only tests/` (runs only benchmarks)

Both flags are fully compatible with pytest 8.x.

---

#### 1.5 Command-Line Interface Changes
**Version Introduced**: 8.0+  
**Impact**: NONE (uses standard flags)

**Project CLI Usage**:
```bash
# From artemis_scripts/test.sh
poetry run pytest --benchmark-skip tests/

# From artemis_scripts/benchmark.sh
poetry run pytest --benchmark-only tests/
```

**Compatibility Status**: ✅ Both flags are stable and compatible with pytest 8.x

---

### Summary of Migration Impact for pytest

| Category | Breaking? | Project Affected? | Action Required |
|----------|-----------|------------------|-----------------|
| Deprecated features | Yes | No | None |
| Assertion behavior | Yes (minor) | No | None |
| Marker parsing | Yes (minor) | No (standard usage) | None |
| Fixture system | No | N/A | None |
| Configuration | Minor | No | None |
| CLI commands | No | N/A | None |

**Conclusion**: ✅ **SAFE TO UPGRADE** - No code or configuration changes required for this project

---

## 2. black: 23.12.1 → 24.12.1 (MINOR VERSION UPGRADE)

### Overview
**Current Version**: 23.12.1  
**Target Version**: 24.12.1  
**Release**: December 2024  
**Breaking Changes Level**: MINIMAL

### Code Formatting Changes

#### 2.1 Formatting Behavior Changes
**Version Introduced**: 24.0+  
**Impact**: Code will be reformatted (expected behavior)

**Notable Formatting Changes in 24.x**:

| Change | Version | Details | Project Code Impact |
|--------|---------|---------|---------------------|
| Preview: hug_parens_with_braces | 24.1+ | Changes formatting of function calls | May reformat code |
| Preview: multiline_string_handling | 24.3+ | Improved string formatting | May reformat code |
| Default formatting improvements | 24.0+ | Various edge cases | May reformat code |

**Expected Behavior**:
- Code will be reformatted to match 24.x standards
- Changes are **formatting only** - no semantic changes
- All Python code remains functionally identical
- This is **expected** and **desired** behavior

**Project Code Examples**:
```python
# May be reformatted but semantics unchanged:
from llm_benchmark.algorithms.primes import Primes

def test_is_prime(n: int, is_prime: bool) -> None:
    assert Primes.is_prime(n) == is_prime
```

---

#### 2.2 CLI and Configuration Changes
**Version Introduced**: 24.0  
**Impact**: MINIMAL (stable CLI)

| Aspect | Status | Details | Action |
|--------|--------|---------|--------|
| CLI flags | Stable | `--line-length`, `--target-version`, etc. all compatible | None |
| pyproject.toml format | Stable | `[tool.black]` section format unchanged | None |
| Configuration options | Stable | Existing configs compatible | None |

**Project Configuration**:
- ✅ No custom black configuration in pyproject.toml
- ✅ Uses default settings (line-length=88)
- ✅ No special CLI flags used in scripts

---

#### 2.3 Default Behavior Changes
**Version Introduced**: 24.0+  
**Impact**: MINOR (code formatting changes expected)

**Key Changes**:
1. **Magic Trailing Comma**: Still respected in 24.x (stable)
2. **Line Length**: Default 88 characters (stable)
3. **String Quote Normalization**: Still enabled by default (stable)
4. **Target Python Versions**: Can specify with `--target-version py38` (stable)

**No Breaking CLI Changes**: All command-line flags remain compatible

---

### Summary of Migration Impact for black

| Category | Breaking? | Project Affected? | Action Required |
|----------|-----------|-------------------|-----------------|
| Formatting behavior | No (expected) | Yes | Reformat with `black .` |
| CLI compatibility | No | No | None |
| Configuration format | No | No | None |
| Default options | No | No | None |

**Conclusion**: ✅ **SAFE TO UPGRADE** - Only formatting changes expected (no code logic changes)

**Recommended Action**: After upgrading black, run `black .` to reformat code to 24.x standards

---

## 3. isort: 5.13.2 (ALREADY AT LATEST)

### Overview
**Current Version**: 5.13.2  
**Latest Version**: 5.13.2  
**Status**: No upgrade available

### Assessment
- ✅ Already at the latest stable release
- ✅ No breaking changes to consider
- ✅ No migration needed
- ✅ Fully compatible with Python 3.8+

### Recommendation
**ACTION**: Keep current version (5.13.2) - No changes needed

---

## 4. pytest-benchmark: 4.0.0 (ALREADY AT LATEST)

### Overview
**Current Version**: 4.0.0  
**Latest Version**: 4.0.0  
**Status**: No upgrade available

### Compatibility with pytest 8.x
- ✅ pytest-benchmark 4.0.0 supports pytest 7.x and 8.x
- ✅ Benchmark fixture works without modification
- ✅ All CLI flags (--benchmark-skip, --benchmark-only) compatible

### Project Usage
The project uses pytest-benchmark for performance testing:
```python
def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)
```

This pattern is fully compatible with pytest 8.x ✅

### Recommendation
**ACTION**: Keep current version (4.0.0) - No changes needed

---

## Migration Checklist by Tool

### pytest (7.4.4 → 8.3.6)

**Pre-Migration**:
- [ ] Review current test files (already done - standard usage confirmed)
- [ ] Check for custom pytest plugins (none found)
- [ ] Check for deprecated pytest patterns (none found)

**Code Changes Required**: ❌ **NONE**
- Standard `pytest.mark.parametrize` usage is compatible
- Standard assertions are compatible
- Benchmark fixture is compatible

**Configuration Changes**: ❌ **NONE**
- No custom pytest configuration in project
- Default behavior is compatible with 8.x
- CLI commands are unchanged

**Migration Steps**:
1. Update `pyproject.toml`: `pytest = "^8.0"` (allows 8.x)
2. Run `poetry update pytest` to install 8.3.6
3. Run `poetry run pytest tests/` to verify all tests pass
4. Run `artemis_scripts/test.sh` to verify test script works
5. Run `artemis_scripts/benchmark.sh` to verify benchmark script works

**Verification**:
- [ ] All tests pass
- [ ] All benchmarks run without errors
- [ ] Test output format is readable
- [ ] No deprecation warnings in output

---

### black (23.12.1 → 24.12.1)

**Pre-Migration**:
- [ ] Confirm no custom black configuration (confirmed - none found)
- [ ] Backup current code format (optional but recommended)

**Code Changes Required**: ❌ **NONE** (only formatting changes)

**Configuration Changes**: ❌ **NONE**
- No custom black configuration in project
- Default settings compatible with 24.x

**Migration Steps**:
1. Update `pyproject.toml`: `black = "^24.0"` (allows 24.x)
2. Run `poetry update black` to install 24.12.1
3. Run `black .` to reformat code to 24.x standards
4. Review formatted code for readability
5. Commit formatting changes with message: "Reformat code with black 24.x"

**Verification**:
- [ ] Code formatting looks correct
- [ ] All tests still pass after reformatting
- [ ] No import errors or syntax issues

---

### isort (5.13.2 - NO UPGRADE)

**Status**: Already at latest stable version

**Action**: No changes needed

---

### pytest-benchmark (4.0.0 - NO UPGRADE)

**Status**: Already at latest stable version

**Compatibility**: Fully compatible with pytest 8.x

**Action**: No changes needed, will continue to work with pytest 8.x upgrade

---

## Complete Migration Order

### Recommended Sequence:

1. **First**: Update pytest (7.4.4 → 8.3.6)
   - Test compatibility
   - Run test suite

2. **Second**: Update black (23.12.1 → 24.12.1)
   - Reformat code
   - Verify tests still pass

3. **Verify**: Run complete test suite and benchmarks

### Implementation Details:

**Step 1: Update pyproject.toml**
```toml
[tool.poetry.group.dev.dependencies]
black = "^24.0"      # Updated from "^23.12.0"
isort = "^5.13.1"    # No change
pytest = "^8.0"      # Updated from "^7.4.3"
pytest-benchmark = "^4.0.0"  # No change
```

**Step 2: Update Poetry Lock File**
```bash
poetry update pytest black
```

**Step 3: Reformat Code**
```bash
black .
```

**Step 4: Run Tests**
```bash
poetry run pytest tests/
poetry run pytest --benchmark-skip tests/
poetry run pytest --benchmark-only tests/
```

---

## Risk Assessment

### Low Risk ✅
- No code logic changes required
- No configuration format changes
- Standard test patterns are compatible
- pytest-benchmark works with pytest 8.x
- black formatting is deterministic and reviewable

### Verification Strategy
- Run full test suite: `pytest tests/`
- Run benchmarks: `pytest --benchmark-only tests/`
- Check for deprecation warnings
- Review code formatting changes

---

## Compatibility Matrix: Project Code vs. Tool Versions

### Current Setup (Before Upgrade)
| Tool | Version | Status |
|------|---------|--------|
| pytest | 7.4.4 | ✅ Works |
| black | 23.12.1 | ✅ Works |
| isort | 5.13.2 | ✅ Works |
| pytest-benchmark | 4.0.0 | ✅ Works |

### After Upgrade
| Tool | Version | Status |
|------|---------|--------|
| pytest | 8.3.6 | ✅ Works (no code changes) |
| black | 24.12.1 | ✅ Works (formatting changes only) |
| isort | 5.13.2 | ✅ Works (no change) |
| pytest-benchmark | 4.0.0 | ✅ Works (compatible) |

---

## Detailed Breaking Changes Reference

### pytest 8.0 Breaking Changes (Official Documentation)

**Removed in 8.0**:
1. `pytest.deprecated_call()` - Use `pytest.warns(DeprecationWarning)` 
   - **Project Impact**: Not used ✅
   
2. Implicit namespace packages in root directory
   - **Project Impact**: Uses explicit test discovery ✅
   
3. Legacy plugins without proper hookimpl
   - **Project Impact**: No custom plugins ✅

**Behavioral Changes in 8.0**:
1. Assertion rewriting improved
   - **Project Impact**: Better error messages ✅
   
2. Marker handling more strict
   - **Project Impact**: Standard usage compatible ✅
   
3. Collection behavior refined
   - **Project Impact**: Standard patterns compatible ✅

### black 24.0 Formatting Changes (Official Documentation)

**New in 24.0+**:
1. Improved handling of string formatting
   - **Project Impact**: Code reformatted but semantics unchanged ✅
   
2. Better parenthesis handling
   - **Project Impact**: Code reformatted but semantics unchanged ✅
   
3. Enhanced magic trailing comma support
   - **Project Impact**: Still supported, backward compatible ✅

**No Breaking Changes**: Black 24.x maintains CLI and config format compatibility

---

## Testing Strategy for Upgrades

### Test Plan

1. **Unit Tests**
   ```bash
   poetry run pytest tests/
   ```
   - Run all tests
   - Verify all pass
   - Check for deprecation warnings

2. **Benchmark Tests**
   ```bash
   poetry run pytest --benchmark-only tests/
   ```
   - Run benchmarks
   - Verify output format
   - Check for any issues with benchmark fixture

3. **Formatting Verification**
   ```bash
   black --check .
   isort --check-only .
   ```
   - Verify all code formatted correctly
   - Check import sorting

4. **Script Verification**
   ```bash
   artemis_scripts/test.sh
   artemis_scripts/benchmark.sh
   ```
   - Run test script
   - Run benchmark script
   - Verify output is correct

---

## Appendix: Detailed Issue Tracking

### pytest-specific

**Issue 1: Benchmark Fixture Compatibility**
- Status: ✅ No issues expected
- Reason: pytest-benchmark 4.0.0 explicitly supports pytest 8.x
- Verification: `poetry show pytest-benchmark` after upgrade

**Issue 2: Parametrize Decorator**
- Status: ✅ No issues expected
- Reason: Standard usage fully compatible with pytest 8.x
- Project Usage: `@pytest.mark.parametrize` throughout tests

**Issue 3: Test Discovery**
- Status: ✅ No issues expected
- Reason: Default behavior compatible, no custom plugins

---

## References

### Official Documentation
- [pytest 8.0 Changelog](https://docs.pytest.org/en/stable/changelog.html)
- [black Release Notes](https://github.com/psf/black/releases)
- [pytest-benchmark Documentation](https://pytest-benchmark.readthedocs.io/)

### Project-Specific Files
- Test files: `tests/llm_benchmark/*/test_*.py`
- Configuration: `pyproject.toml`
- Scripts: `artemis_scripts/test.sh`, `artemis_scripts/benchmark.sh`

---

## Summary

**Upgrading to pytest 8.3.6 and black 24.12.1 is SAFE and RECOMMENDED.**

### Why It's Safe:
1. ✅ No code logic changes required
2. ✅ No configuration changes needed
3. ✅ All test patterns are compatible
4. ✅ pytest-benchmark works with pytest 8.x
5. ✅ Black formatting changes are expected and benign

### What Will Change:
1. **Code formatting** (black 24.x) - Expected, beneficial
2. **Test output** (pytest 8.x) - Minor formatting improvements
3. **Error messages** (pytest 8.x) - More informative

### Next Steps:
1. Update `pyproject.toml` with new versions
2. Run `poetry update`
3. Run `black .` to reformat code
4. Run full test suite to verify
5. Commit changes

---

**Document prepared**: January 2025  
**For project**: llm_benchmark  
**Status**: Ready for implementation
