from sys import maxsize
from typing import List


class Sort:
    @staticmethod
    def sort_list(v: List[int]) -> None:
        """Sort a list of integers in place using quicksort

        Args:
            v (List[int]): List of integers
        """
        def quicksort(arr: List[int], low: int, high: int) -> None:
            """Helper function to recursively sort the list using quicksort
            
            Args:
                arr: List to sort
                low: Starting index
                high: Ending index
            """
            if low < high:
                # Partition and get the pivot index
                pivot_index = partition(arr, low, high)
                # Recursively sort left and right partitions
                quicksort(arr, low, pivot_index - 1)
                quicksort(arr, pivot_index + 1, high)
        
        def partition(arr: List[int], low: int, high: int) -> int:
            """Partition the array around a pivot
            
            Args:
                arr: List to partition
                low: Starting index
                high: Ending index
                
            Returns:
                int: Index of the pivot element after partitioning
            """
            # Choose the middle element as pivot to avoid worst case on sorted arrays
            mid = (low + high) // 2
            arr[mid], arr[high] = arr[high], arr[mid]
            pivot = arr[high]
            
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        if len(v) > 1:
            quicksort(v, 0, len(v) - 1)

    @staticmethod
    def dutch_flag_partition(v: List[int], pivot_value: int) -> None:
        """Dutch flag partitioning

        Args:
            v (List[int]): List of integers
            pivot_value (int): Pivot value
        """
        next_value = 0

        for i in range(len(v)):
            if v[i] < pivot_value:
                v[i], v[next_value] = v[next_value], v[i]
                next_value += 1
        for i in range(next_value, len(v)):
            if v[i] == pivot_value:
                v[i], v[next_value] = v[next_value], v[i]
                next_value += 1

    @staticmethod
    def max_n(v: List[int], n: int) -> List[int]:
        """Find the maximum n numbers in a list

        Args:
            v (List[int]): List of integers
            n (int): Number of maximum values to find

        Returns:
            List[int]: List of maximum n values
        """
        tmp = v.copy()
        ret = [-maxsize - 1] * n
        for i in range(n):
            max_val = tmp[0]
            max_idx = 0
            for j in range(1, len(tmp)):
                if tmp[j] > max_val:
                    max_val = tmp[j]
                    max_idx = j
            ret[i] = max_val
            tmp.pop(max_idx)
        return ret
