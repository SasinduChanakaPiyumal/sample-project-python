from typing import List

import pytest

from llm_benchmark.algorithms.primes import Primes, MAX_PRIMES_BOUND


@pytest.mark.parametrize(
    "n, is_prime",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (10, False),
        (17, True),
        (26, False),
    ],
)
def test_is_prime(n: int, is_prime: bool) -> None:
    assert Primes.is_prime(n) == is_prime


def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)


@pytest.mark.parametrize(
    "n, S", [(0, 0), (1, 0), (2, 0), (3, 2), (4, 5), (10, 17), (100, 1060)]
)
def test_sum_primes(n: int, S: int) -> None:
    assert Primes.sum_primes(n) == S


def test_benchmark_sum_primes(benchmark) -> None:
    benchmark(Primes.sum_primes, 20)


def test_sum_primes_boundary_max_minus_one() -> None:
    """Test sum_primes at the upper boundary (MAX_PRIMES_BOUND - 1) should succeed."""
    # This should succeed without raising an exception
    result = Primes.sum_primes(MAX_PRIMES_BOUND - 1)
    # Just verify it returns an integer (actual value is not critical for this test)
    assert isinstance(result, int)
    assert result > 0


def test_sum_primes_boundary_max_exact() -> None:
    """Test sum_primes at exactly MAX_PRIMES_BOUND should raise ValueError."""
    with pytest.raises(ValueError):
        Primes.sum_primes(MAX_PRIMES_BOUND)


def test_sum_primes_boundary_max_plus_one() -> None:
    """Test sum_primes above MAX_PRIMES_BOUND should raise ValueError."""
    with pytest.raises(ValueError):
        Primes.sum_primes(MAX_PRIMES_BOUND + 1)


@pytest.mark.parametrize(
    "n",
    [10**6, 10**7, 10**8, 10**9],
)
def test_sum_primes_large_inputs_rejected(n: int) -> None:
    """Test that large inputs (10^6, 10^7, 10^8, 10^9) are rejected with ValueError."""
    with pytest.raises(ValueError):
        Primes.sum_primes(n)


def test_sum_primes_error_message_contains_constraint() -> None:
    """Test that ValueError message indicates the constraint and limit."""
    with pytest.raises(ValueError) as exc_info:
        Primes.sum_primes(MAX_PRIMES_BOUND + 1)
    
    error_message = str(exc_info.value)
    # Verify error message contains key constraint information
    assert "exceeds maximum allowed bound" in error_message
    assert str(MAX_PRIMES_BOUND) in error_message or f"{MAX_PRIMES_BOUND:,}" in error_message
    assert "resource exhaustion" in error_message


@pytest.mark.parametrize(
    "n, factors",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (10, [2, 5]),
        (17, [17]),
        (84, [2, 2, 3, 7]),
    ],
)
def test_prime_factors(n: int, factors: List[int]) -> None:
    assert Primes.prime_factors(n) == factors


def test_benchmark_prime_factors(benchmark) -> None:
    benchmark(Primes.prime_factors, 84)
