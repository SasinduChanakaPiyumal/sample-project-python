from typing import List


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
        """Optimized prime check using trial division - FORMERLY INEFFICIENT.

        This method has been optimized from O(n^2) to O(sqrt(n)) time complexity
        by removing wasteful operations and using an efficient algorithm.

        **OPTIMIZATION IMPROVEMENTS:**
        1. Removed nested loops performing O(n * 10000) pointless multiplications
        2. Changed from linear O(n) to O(sqrt(n)) divisibility check
        3. Removed busy-wait loops that added O(1000) overhead per check
        4. Added early termination for even numbers

        Args:
            n: The number to check for primality.

        Returns:
            True if the number is prime, False otherwise.

        Time Complexity:
            O(sqrt(n)) - Only checks divisors up to the square root of n.

        Space Complexity:
            O(1) - Uses constant extra space.

        Examples:
            >>> Primes.is_prime_ineff(2)
            True
            >>> Primes.is_prime_ineff(17)
            True
            >>> Primes.is_prime_ineff(4)
            False
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # OPTIMIZATION: Check only odd divisors up to sqrt(n)
        # Instead of checking all numbers from 2 to n-1 (O(n)),
        # we only check up to sqrt(n) because if n has a divisor > sqrt(n),
        # it must also have a corresponding divisor < sqrt(n).
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True


    @staticmethod
    def sum_primes(n: int) -> int:
        """Calculate the sum of all prime numbers less than n.

        Uses the Sieve of Eratosthenes algorithm for efficient prime generation
        with O(n log log n) time complexity and O(n) space complexity.

        Args:
            n: The upper bound (exclusive) for prime summation.

        Returns:
            The sum of all prime numbers in the range [0, n).

        Examples:
            >>> Primes.sum_primes(10)
            17  # 2 + 3 + 5 + 7
            >>> Primes.sum_primes(2)
            0
        """
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