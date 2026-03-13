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
        """
        return [randint(0, m - 1) for _ in range(n)]

    @staticmethod
    def random_matrix(rows: int, cols: int, max_value: int) -> List[List[int]]:
        """Generate a matrix of random integers

        Args:
            rows (int): Number of rows
            cols (int): Number of columns
            max_value (int): Maximum value of integers (exclusive)

        Returns:
            List[List[int]]: Matrix of random integers
        """
        return [GenList.random_list(cols, max_value) for _ in range(rows)]