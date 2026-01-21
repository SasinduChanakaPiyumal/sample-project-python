from collections import Counter
from typing import List


class DoubleForLoop:
    @staticmethod
    def sum_square(n: int) -> int:
        """Sum of squares of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of squares of numbers from 0 to n
        """
        # Use mathematical formula for sum of squares: 0^2 + 1^2 + ... + (n-1)^2
        # Formula: (n-1) * n * (2*n - 1) // 6
        return (n - 1) * n * (2 * n - 1) // 6

    @staticmethod
    def sum_triangle(n: int) -> int:
        """Sum of triangle of numbers from 0 to n (exclusive)

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of triangle of numbers from 0 to n
        """
        sum_ = 0
        for i in range(n):
            for j in range(i + 1):
                sum_ += j
        return sum_

    @staticmethod
    def count_pairs(arr: List[int]) -> int:
        """Count pairs of numbers in an array

        A pair is defined as exactly two numbers in the array that are equal.

        Args:
            arr (List[int]): Array of integers

        Returns:
            int: Number of pairs in the array
        """
        # Count frequency of each element in O(N) time
        freq_map = Counter(arr)
        
        # Count elements that appear exactly twice
        count = sum(1 for freq in freq_map.values() if freq == 2)
        
        return count

    @staticmethod
    def count_duplicates(arr0: List[int], arr1: List[int]) -> int:
        """Count duplicates between two arrays

        Args:
            arr0 (List[int]): Array of integers
            arr1 (List[int]): Array of integers

        Returns:
            int: Number of duplicates between the two arrays
        """
        try:
            len0 = len(arr0)
            len1 = len(arr1)
        except TypeError:
            # Fall back to a zip-based comparison for iterables without __len__
            return sum(1 for left, right in zip(arr0, arr1) if left == right)

        if not len0 or not len1:
            return 0

        min_len = len0 if len0 < len1 else len1
        return sum(1 for idx in range(min_len) if arr0[idx] == arr1[idx])

    @staticmethod
    def sum_matrix(m: List[List[int]]) -> int:
        """Sum of matrix of integers

        Args:
            m (List[List[int]]): Matrix of integers

        Returns:
            int: Sum of matrix of integers
        """
        sum_ = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                sum_ += m[i][j]
        return sum_
