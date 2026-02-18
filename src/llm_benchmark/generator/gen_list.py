from random import randint
from typing import List


class GenList:
    @staticmethod
    def random_list(n: int, m: int) -> List[int]:
        """Generate a list of random integers

        Args:
            n (int): Number of integers to generate
            m (int): Maximum value of integers (exclusive)

        Returns:
            List[int]: List of random integers
            
        Security Note:
            Uses Python's random module for non-cryptographic purposes only.
            For security-sensitive random generation, use secrets module instead.
        """
        # SECURITY FIX: randint(0, m) was inclusive on both ends, but docstring
        # promised exclusive upper bound. Changed to randint(0, m-1) to match
        # the documented contract. This prevents out-of-bounds errors when
        # values are used as array indices or in range-constrained logic.
        return [randint(0, m - 1) for _ in range(n)]

    @staticmethod
    def random_matrix(n: int, m: int) -> List[List[int]]:
        """Generate a matrix of random integers

        Args:
            n (int): Number of rows
            m (int): Maximum value of integers (exclusive)

        Returns:
            List[List[int]]: Matrix of random integers
        """
        # Generate n rows, each with n integers from 0 to m-1 (exclusive)
        return [GenList.random_list(n, m) for _ in range(n)]
