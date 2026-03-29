from typing import List


# ========================================================================================
# SECURITY: Maximum bound for sum_primes() - CWE-400 Resource Exhaustion Mitigation
# ========================================================================================
# 
# VULNERABILITY (CWE-400 - Uncontrolled Resource Consumption):
# The Sieve of Eratosthenes algorithm allocates a list of n booleans to track prime status.
# Without a hard upper bound, an attacker could request sums for extremely large values,
# causing uncontrolled memory allocation and system resource exhaustion (denial-of-service).
#
# RATIONALE FOR THIS SPECIFIC LIMIT (10,000,000):
# A list of 10 million booleans consumes approximately 100MB of memory on typical systems,
# representing a reasonable upper bound for this utility function. This limit:
# - Allows calculations up to 10 million without taxing most systems
# - Clearly rejects obviously malicious or resource-hungry requests
# - Provides protection against unintended excessive usage
#
# MEMORY IMPACT PROGRESSION (system-dependent, approximate):
# - n = 10^7  (10,000,000):   ~100 MB  ✓ Acceptable
# - n = 10^8  (100,000,000):  ~1 GB    ✗ Excessive
# - n = 10^9  (1,000,000,000): ~8 GB+   ✗ System failure risk
#
# DESIGN CHOICE: Why a hard limit instead of configuration/algorithm replacement?
# See SECURITY.md at project root for full rationale. In summary:
# - Hard limit is deterministic and cannot be accidentally bypassed
# - Configurability adds complexity and potential for misconfiguration
# - Algorithm replacement (e.g., segmented sieve) adds significant complexity
#   with diminishing returns for the legitimate use cases of this function
# - Input validation before allocation is the most effective DoS mitigation
#
# REFERENCE: See SECURITY.md for comprehensive vulnerability analysis and mitigation strategy
MAX_PRIMES_BOUND = 10_000_000


class Primes:
    """Collection of prime number algorithms including efficient and benchmark variants."""

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime using trial division.

        Uses an optimized O(sqrt(n)) algorithm that checks divisibility only by
        2 and odd numbers up to the square root of n.

        Args:
            n: The number to check for primality.

        Returns:
            True if the number is prime, False otherwise.

        Examples:
            >>> Primes.is_prime(2)
            True
            >>> Primes.is_prime(17)
            True
            >>> Primes.is_prime(4)
            False
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Check odd divisors up to sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Deliberately inefficient prime check for benchmarking and education.

        **WARNING: NOT FOR PRODUCTION USE**

        This method intentionally uses O(n^2) time complexity through wasteful
        nested loops and redundant calculations. It serves as a baseline for
        performance comparisons against the optimized is_prime() method.

        **Use cases:**
        - Performance benchmarking vs optimized algorithms
        - Educational demonstrations of anti-patterns
        - Showing the impact of inefficient implementations

        **Deliberate inefficiencies:**
        1. Nested loops performing O(n * 10000) pointless multiplications
        2. Linear divisibility check O(n) instead of O(sqrt(n))
        3. Busy-wait loop adding O(1000) overhead per divisibility check

        Args:
            n: The number to check for primality.

        Returns:
            True if the number is prime, False otherwise.

        Time Complexity:
            O(n^2) - Dominated by nested wasteful loops. The actual primality
            test is buried under layers of unnecessary computation.

        Examples:
            >>> Primes.is_prime_ineff(2)
            True
            >>> Primes.is_prime_ineff(4)
            False
        """
        if n < 2:
            return False

        # INEFFICIENCY #1: Nested loops with pointless calculations O(n * 10000)
        # Wastes CPU cycles on multiplications unrelated to primality testing.
        # AVOIDED: Skipping this entirely (as done in is_prime).
        for j in range(1, n):
            for k in range(1, 10000):
                _ = k * j  # Arbitrary multiplication with no purpose

        # INEFFICIENCY #2: Linear divisibility check O(n) instead of O(sqrt(n))
        # Checks ALL divisors from 2 to n-1 instead of stopping at sqrt(n).
        # 
        # Comparison to is_prime():
        # - Optimized: "i * i <= n" stops at sqrt(n) → O(sqrt(n))
        # - Inefficient: "range(2, n)" checks all → O(n)
        # 
        # For n=100: optimized checks ~10 divisors, this checks 98 divisors.
        # AVOIDED: Using "i * i <= n" termination condition.
        for i in range(2, n):
            # INEFFICIENCY #3: Busy-wait loop O(1000) before each check
            # Wastes 1000 iterations doing nothing, multiplying the O(n)
            # divisibility checks by O(1000), pushing toward O(n^2).
            # AVOIDED: Immediate divisibility checking without delays.
            for _ in range(1000):
                pass  # Pure time waste

            # The ONLY useful operation: actual primality test
            if n % i == 0:
                return False

        return True


    @staticmethod
    def sum_primes(n: int) -> int:
        """Calculate the sum of all prime numbers less than n.

        Uses the Sieve of Eratosthenes algorithm for efficient prime generation
        with O(n log log n) time complexity and O(n) space complexity.

        **Security Note (CWE-400):**
        This function implements a resource exhaustion defense by enforcing an upper
        bound on input values. The limit of 10,000,000 prevents denial-of-service (DoS)
        attacks where untrusted callers could request sums for extremely large bounds,
        exhausting system memory with large list allocations.

        Args:
            n: The upper bound (exclusive) for prime summation. Must be in the range
               [0, 10,000,000). Values exceeding this limit are rejected to prevent
               resource exhaustion attacks.

        Returns:
            The sum of all prime numbers in the range [0, n).

        Raises:
            ValueError: If n exceeds the maximum allowed bound (10,000,000). This
                       indicates an invalid input that could lead to excessive memory
                       allocation or denial-of-service conditions.

        Examples:
            Valid usage:

            >>> Primes.sum_primes(10)
            17  # 2 + 3 + 5 + 7
            >>> Primes.sum_primes(100)
            1060

            Invalid usage (exceeds bounds):

            >>> Primes.sum_primes(10_000_001)  # doctest: +SKIP
            Traceback (most recent call last):
                ...
            ValueError: Input value n (10,000,001) exceeds maximum allowed bound (10,000,000)...
        """
        # ======================================================================================
        # SECURITY VALIDATION: CWE-400 Resource Exhaustion Defense
        # ======================================================================================
        # This check MUST occur BEFORE any memory allocation (specifically before the
        # "is_prime = [True] * n" list allocation below). Validating input boundaries before
        # resource allocation is critical for preventing denial-of-service (DoS) attacks.
        #
        # ATTACK PREVENTED:
        # Without this validation, an attacker could call sum_primes(10^9) causing the
        # allocation of ~8GB+ of memory, exhausting system resources and causing a denial
        # of service. The validation rejects such requests immediately without consuming
        # significant resources.
        #
        # WHY THIS DEFENSE IS NECESSARY:
        # - CWE-400 (Uncontrolled Resource Consumption) is a category A vulnerability
        # - Untrusted callers could submit arbitrarily large values
        # - The Sieve of Eratosthenes has O(n) space complexity - no algorithmic fix possible
        # - Input validation is the most effective and robust mitigation
        #
        # IMPLEMENTATION DETAIL:
        # The check uses MAX_PRIMES_BOUND (10,000,000) as the deterministic upper limit.
        # See the MAX_PRIMES_BOUND constant definition above for security rationale.
        # ======================================================================================
        if n > MAX_PRIMES_BOUND:
            raise ValueError(
                f"Input value n ({n:,}) exceeds maximum allowed bound "
                f"({MAX_PRIMES_BOUND:,}). This limit exists to prevent resource "
                f"exhaustion attacks and excessive memory allocation."
            )
        
        if n <= 2:
            return 0
        
        # Sieve of Eratosthenes: mark composite numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Only need to check up to sqrt(n)
        sqrt_n = int(n ** 0.5)
        for i in range(2, sqrt_n + 1):
            if is_prime[i]:
                # Mark all multiples of i starting from i^2 as composite
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Sum all remaining prime numbers
        return sum(i for i in range(n) if is_prime[i])

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Compute the prime factorization of a number.

        Returns all prime factors (with repetition) in ascending order.
        Uses trial division with O(sqrt(n)) time complexity.

        Args:
            n: The number to factorize (must be positive).

        Returns:
            A list of prime factors in ascending order. Returns an empty list
            for n <= 1.

        Examples:
            >>> Primes.prime_factors(12)
            [2, 2, 3]
            >>> Primes.prime_factors(17)
            [17]
            >>> Primes.prime_factors(1)
            []
        """
        if n <= 1:
            return []
        
        factors = []
        
        # Extract all factors of 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check odd divisors starting from 3 up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If n > 1 after division, it's a prime factor itself
        if n > 1:
            factors.append(n)
        
        return factors