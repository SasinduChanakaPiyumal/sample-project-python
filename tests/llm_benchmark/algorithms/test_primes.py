from typing import List

import pytest

from llm_benchmark.algorithms.primes import Primes


# Test for the is_prime method with various edge cases and standard values
@pytest.mark.parametrize(
    "n, is_prime",
    [
        (0, False),  # Test edge case: 0 is not prime
        (1, False),  # Test edge case: 1 is not prime
        (2, True),   # Test edge case: 2 is the smallest prime
        (3, True),   # Test small prime
        (4, False),  # Test composite number
        (10, False), # Test even composite number
        (17, True),  # Test larger prime
        (26, False), # Test larger composite number
    ],
)
def test_is_prime(n: int, is_prime: bool) -> None:
    # Verify that is_prime correctly identifies primes and non-primes
    assert Primes.is_prime(n) == is_prime


def test_benchmark_is_prime(benchmark) -> None:
    # Benchmark the is_prime method with a prime number
    benchmark(Primes.is_prime, 17)


# Test for the sum_primes method that sums all primes less than n
@pytest.mark.parametrize(
    "n, S", [
        (0, 0),       # Test edge case: no primes less than 0
        (1, 0),       # Test edge case: no primes less than 1
        (2, 0),       # Test edge case: no primes less than 2
        (3, 2),       # Test: only 2 is prime, sum = 2
        (4, 5),       # Test: 2 and 3 are prime, sum = 5
        (10, 17),     # Test: 2+3+5+7 = 17
        (100, 1060)   # Test: sum of all primes less than 100
    ]
)
def test_sum_primes(n: int, S: int) -> None:
    # Verify that sum_primes correctly calculates the sum of all primes less than n
    assert Primes.sum_primes(n) == S


def test_benchmark_sum_primes(benchmark) -> None:
    # Benchmark the sum_primes method with n=20
    benchmark(Primes.sum_primes, 20)


# Test for the prime_factors method that returns prime factorization of a number
@pytest.mark.parametrize(
    "n, factors",
    [
        (0, []),           # Test edge case: 0 has no prime factors
        (1, []),           # Test edge case: 1 has no prime factors
        (2, [2]),          # Test: 2 is prime
        (3, [3]),          # Test: 3 is prime
        (4, [2, 2]),       # Test: 4 = 2 * 2
        (10, [2, 5]),      # Test: 10 = 2 * 5
        (17, [17]),        # Test: 17 is prime
        (84, [2, 2, 3, 7]), # Test: 84 = 2 * 2 * 3 * 7, composite number with multiple factors
    ],
)
def test_prime_factors(n: int, factors: List[int]) -> None:
    # Verify that prime_factors returns the correct prime factorization in order
    assert Primes.prime_factors(n) == factors


def test_benchmark_prime_factors(benchmark) -> None:
    # Benchmark the prime_factors method with n=84
    benchmark(Primes.prime_factors, 84)
