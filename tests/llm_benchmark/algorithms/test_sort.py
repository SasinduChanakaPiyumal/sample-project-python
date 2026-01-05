from typing import List

import pytest

from llm_benchmark.algorithms.sort import Sort


@pytest.mark.parametrize(
    "v, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [5, 4]),
        ([5, 4, 3, 2, 1], 3, [5, 4, 3]),
        ([3, 1, 4, 1, 5], 2, [5, 4]),
    ],
)
def test_max_n_normal_cases(v: List[int], n: int, expected: List[int]) -> None:
    """Test max_n with normal cases where n <= len(v)"""
    assert Sort.max_n(v, n) == expected


@pytest.mark.parametrize(
    "v, n",
    [
        ([1, 2, 3], 5),  # n > len(v)
        ([10], 2),  # n > len(v)
        ([1, 2, 3, 4, 5], 10),  # n >> len(v)
    ],
)
def test_max_n_edge_cases(v: List[int], n: int) -> None:
    """Test max_n with edge cases where n > len(v)"""
    # Should not raise an error
    result = Sort.max_n(v, n)
    # Result should have length n
    assert len(result) == n
    # First min(n, len(v)) elements should be the largest values
    filled_positions = min(n, len(v))
    # Check that the filled positions contain the sorted values
    sorted_v = sorted(v, reverse=True)
    for i in range(filled_positions):
        assert result[i] == sorted_v[i]
