"""
Security tests for GenList random number generation.

This test suite demonstrates a security vulnerability fix:
- VULNERABILITY: randint(0, m) is inclusive on both ends, but the docstring
  documented it as exclusive upper bound
- IMPACT: If values are used as array indices or in range-constrained logic,
  this could cause out-of-bounds errors or security violations
- FIX: Changed to randint(0, m-1) to match the documented contract (exclusive)

The fix ensures that for a parameter m, values returned are always in [0, m-1],
never reaching or exceeding m.
"""
import pytest
from llm_benchmark.generator.gen_list import GenList


class TestRandomListExclusiveUpperBound:
    """Test that random_list respects the exclusive upper bound contract."""
    
    def test_random_list_values_within_exclusive_range(self):
        """
        SECURITY TEST: Verify that random_list returns values strictly less than m.
        
        This test demonstrates the vulnerability is fixed. Before the fix,
        randint(0, m) could return values equal to m, violating the documented
        "exclusive" contract. This could cause array out-of-bounds errors if
        these values are used as indices.
        """
        m = 10
        n = 1000  # Large sample for statistical confidence
        values = GenList.random_list(n, m)
        
        # All values must be in range [0, m-1] (exclusive upper bound)
        assert all(0 <= v < m for v in values), \
            f"Values exceeded exclusive upper bound of {m}"
        assert min(values) >= 0, "Values must be non-negative"
        assert max(values) < m, f"Values must be strictly less than {m}, found max={max(values)}"
    
    def test_random_list_no_value_equals_m(self):
        """
        SECURITY TEST: Verify no value ever equals the upper bound m.
        
        This specific test checks that the vulnerability (inclusive upper bound)
        is fixed. If someone uses these values as array indices and assumes
        exclusive upper bound based on documentation, an off-by-one error would
        be a serious bug.
        """
        m = 5
        n = 500
        values = GenList.random_list(n, m)
        
        # The critical security check: no value should equal m
        assert all(v != m for v in values), \
            f"SECURITY VIOLATION: Found value equal to m={m}. " \
            f"This violates exclusive upper bound contract and would cause " \
            f"out-of-bounds errors when used as array indices."
    
    def test_random_list_respects_lower_bound(self):
        """Verify random_list respects the inclusive lower bound of 0."""
        m = 10
        n = 1000
        values = GenList.random_list(n, m)
        
        # All values must be >= 0 (inclusive lower bound)
        assert all(v >= 0 for v in values), "Values must be non-negative"
        assert min(values) >= 0, "Minimum value must be >= 0"
    
    def test_random_list_small_range(self):
        """Test with small range to ensure no edge case violations."""
        m = 2
        n = 100
        values = GenList.random_list(n, m)
        
        # With m=2, should only get 0 and 1
        valid_values = {0, 1}
        assert set(values).issubset(valid_values), \
            f"Values must be in {valid_values}, got {set(values)}"
        assert max(values) < m
    
    def test_random_list_length(self):
        """Verify random_list generates correct number of values."""
        n = 50
        m = 10
        values = GenList.random_list(n, m)
        
        assert len(values) == n, f"Expected {n} values, got {len(values)}"
    
    def test_random_matrix_values_within_range(self):
        """
        SECURITY TEST: Verify random_matrix also respects exclusive upper bound.
        
        Since random_matrix uses random_list internally, this tests the
        transitive security guarantee.
        """
        rows = 10
        cols = 10
        m = 5
        matrix = GenList.random_matrix(rows, m)
        
        # Verify matrix structure
        assert len(matrix) == rows, f"Expected {rows} rows, got {len(matrix)}"
        
        # Verify all values respect exclusive upper bound
        for row in matrix:
            assert len(row) == rows, f"Expected {rows} columns, got {len(row)}"
            assert all(0 <= v < m for v in row), \
                f"Values in matrix exceeded exclusive upper bound of {m}"
            assert all(v != m for v in row), \
                f"SECURITY VIOLATION: Found matrix value equal to m={m}"


class TestRandomListBehavioral:
    """Test behavioral aspects of random_list generation."""
    
    def test_random_list_distribution(self):
        """
        Test that random_list produces reasonably distributed values.
        
        With uniform distribution, each value should appear roughly equally
        often over a large sample. This is not a strict security test but
        validates the random generation quality.
        """
        m = 10
        n = 10000
        values = GenList.random_list(n, m)
        
        # Count occurrences of each value
        from collections import Counter
        counts = Counter(values)
        
        # We should see all values from 0 to m-1
        expected_values = set(range(m))
        seen_values = set(counts.keys())
        assert expected_values == seen_values, \
            f"Expected to see all values {expected_values}, but got {seen_values}"
        
        # Each value should appear roughly n/m times (within reasonable bounds)
        expected_count = n / m
        tolerance = expected_count * 0.5  # Allow 50% variation
        
        for value in range(m):
            actual_count = counts[value]
            assert abs(actual_count - expected_count) < tolerance, \
                f"Value {value} appeared {actual_count} times, " \
                f"expected ~{expected_count}"


class TestVulnerabilityDocumentation:
    """
    Document the security vulnerability that was fixed.
    
    VULNERABILITY DESCRIPTION:
    ========================
    
    ISSUE: Off-by-one error in random number generation upper bound
    LOCATION: src/llm_benchmark/generator/gen_list.py, random_list() method
    SEVERITY: Medium
    
    BEFORE (Vulnerable):
        return [randint(0, m) for _ in range(n)]
        
        - randint(0, m) includes both 0 and m (inclusive on both ends)
        - Docstring claims m is "Maximum value (exclusive)"
        - Violates documented contract
        - Can return values up to and including m
    
    AFTER (Secure):
        return [randint(0, m - 1) for _ in range(n)]
        
        - Now returns values in range [0, m-1] only
        - Matches documented contract (exclusive upper bound)
        - Safe to use as array indices with arrays of size m
        - Values never exceed or equal the upper bound
    
    IMPACT SCENARIOS:
    - If used to generate array indices: could cause out-of-bounds errors
    - If used in access control logic: could bypass bounds checks
    - If used for allocation/constraint: could overflow limits
    
    EXPLOITATION:
    The vulnerability is demonstrated in test_random_list_no_value_equals_m()
    which verifies the fix prevents returning values equal to the upper bound.
    """
    pass


def test_vulnerability_comparison():
    """
    Demonstrate that the fixed version correctly implements exclusive upper bound.
    
    This test shows the difference between the vulnerable and fixed versions:
    - Vulnerable: randint(0, m) can return values 0 through m (m+1 possibilities)
    - Fixed: randint(0, m-1) returns values 0 through m-1 (m possibilities)
    """
    from random import randint
    
    m = 10
    n = 10000
    
    # The FIXED version (what we use now)
    fixed_values = GenList.random_list(n, m)
    
    # Verify fixed version never returns m or greater
    assert max(fixed_values) < m, \
        "Fixed version should never return value >= m"
    
    # Verify we can use these as array indices safely
    safe_array = list(range(m))
    for value in fixed_values:
        # This should never raise IndexError
        _ = safe_array[value]
    
    # The vulnerable version would look like:
    # vulnerable = [randint(0, m) for _ in range(n)]
    # And could cause: safe_array[m] -> IndexError
    
    print(f"✓ All {len(fixed_values)} values are in valid range [0, {m-1}]")
    print(f"✓ Max value: {max(fixed_values)}, Min value: {min(fixed_values)}")
    print(f"✓ Safe to use as indices for arrays of size {m}")
