from typing import List


class DsList:
    @staticmethod
    def modify_list(v: List[int]) -> List[int]:
        """Modify a list by adding 1 to each element

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Modified list of integers

        Raises:
            TypeError: If v is not a list or contains non-numeric elements
            ValueError: If v is not a valid list-like object
        """
        if not isinstance(v, list):
            raise TypeError(f"Expected list, got {type(v).__name__}")
        
        try:
            ret = []
            for i in range(len(v)):
                try:
                    ret.append(v[i] + 1)
                except TypeError as e:
                    raise TypeError(f"Element at index {i} cannot be added to integer: {e}")
            return ret
        except (AttributeError, TypeError) as e:
            raise ValueError(f"Invalid list-like object provided: {e}")

    @staticmethod
    def search_list(v: List[int], n: int) -> List[int]:
        """Search a list for a value, returning a list
        of indices where the value is found

        Args:
            v (List[int]): List of integers
            n (int): Value to search for

        Returns:
            List[int]: List of indices where the value is found

        Raises:
            TypeError: If v is not a list or n cannot be compared with list elements
            ValueError: If v is not a valid list-like object
        """
        if not isinstance(v, list):
            raise TypeError(f"Expected list, got {type(v).__name__}")
        
        try:
            ret = []
            for i in range(len(v)):
                try:
                    if v[i] == n:
                        ret.append(i)
                except TypeError as e:
                    raise TypeError(f"Cannot compare element at index {i} with search value: {e}")
            return ret
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Invalid list-like object provided: {e}")

    @staticmethod
    def sort_list(v: List[int]) -> List[int]:
        """Sort a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Sorted list of integers

        Raises:
            TypeError: If v is not a list or contains non-comparable elements
            ValueError: If v is not a valid list-like object
        """
        if not isinstance(v, list):
            raise TypeError(f"Expected list, got {type(v).__name__}")
        
        try:
            ret = v.copy()
        except AttributeError:
            raise ValueError("Provided object does not support copy operation")
        
        try:
            for i in range(len(ret)):
                for j in range(i + 1, len(ret)):
                    if ret[i] > ret[j]:
                        ret[i], ret[j] = ret[j], ret[i]
            return ret
        except TypeError as e:
            raise TypeError(f"Cannot compare list elements: {e}")

    @staticmethod
    def reverse_list(v: List[int]) -> List[int]:
        """Reverse a list of integers, returns a copy

        Args:
            v (List[int]): List of integers

        Returns:
            List[int]: Reversed list of integers

        Raises:
            TypeError: If v is not a list
            ValueError: If v is not a valid list-like object
        """
        if not isinstance(v, list):
            raise TypeError(f"Expected list, got {type(v).__name__}")
        
        try:
            ret = []
            for i in range(len(v)):
                ret.append(v[len(v) - 1 - i])
            return ret
        except (AttributeError, IndexError, TypeError) as e:
            raise ValueError(f"Invalid list-like object provided: {e}")

    @staticmethod
    def rotate_list(v: List[int], n: int) -> List[int]:
        """Rotate a list of integers by n positions

        Args:
            v (List[int]): List of integers
            n (int): Number of positions to rotate

        Returns:
            List[int]: Rotated list of integers

        Raises:
            TypeError: If v is not a list or n is not an integer
            ValueError: If n is negative or out of bounds
        """
        if not isinstance(v, list):
            raise TypeError(f"Expected list, got {type(v).__name__}")
        
        if not isinstance(n, int):
            raise TypeError(f"Expected integer for n, got {type(n).__name__}")
        
        if n < 0:
            raise ValueError(f"Rotation value n must be non-negative, got {n}")
        
        if len(v) > 0 and n > len(v):
            raise ValueError(f"Rotation value n ({n}) cannot exceed list length ({len(v)})")
        
        try:
            ret = []
            for i in range(n, len(v)):
                ret.append(v[i])
            for i in range(n):
                ret.append(v[i])
            return ret
        except (AttributeError, IndexError, TypeError) as e:
            raise ValueError(f"Invalid list-like object provided: {e}")

    @staticmethod
    def merge_lists(v1: List[int], v2: List[int]) -> List[int]:
        """Merge two lists of integers, returns a copy

        Args:
            v1 (List[int]): First list of integers
            v2 (List[int]): Second list of integers

        Returns:
            List[int]: Merged list of integers

        Raises:
            TypeError: If v1 or v2 is not a list
            ValueError: If v1 or v2 is not a valid list-like object
        """
        if not isinstance(v1, list):
            raise TypeError(f"Expected list for v1, got {type(v1).__name__}")
        
        if not isinstance(v2, list):
            raise TypeError(f"Expected list for v2, got {type(v2).__name__}")
        
        try:
            ret = []
            for i in range(len(v1)):
                ret.append(v1[i])
            for i in range(len(v2)):
                ret.append(v2[i])
            return ret
        except (AttributeError, IndexError, TypeError) as e:
            raise ValueError(f"Invalid list-like object provided: {e}")
