from typing import List

import pytest

from llm_benchmark.algorithms.sort import Sort


class TestSortListBasicCases:
    """Test basic functionality of Sort.sort_list() method."""

    def test_empty_list(self) -> None:
        """Test that an empty list remains empty after sorting."""
        lst: List[int] = []
        Sort.sort_list(lst)
        assert lst == []

    def test_single_element(self) -> None:
        """Test that a single element list remains unchanged."""
        lst: List[int] = [42]
        Sort.sort_list(lst)
        assert lst == [42]

    def test_already_sorted(self) -> None:
        """Test that an already sorted list remains sorted."""
        lst: List[int] = [1, 2, 3, 4, 5]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3, 4, 5]

    def test_two_elements_sorted(self) -> None:
        """Test that two sorted elements remain sorted."""
        lst: List[int] = [1, 2]
        Sort.sort_list(lst)
        assert lst == [1, 2]


class TestSortListReverseAndUnsorted:
    """Test reverse sorted and unsorted lists."""

    def test_reverse_sorted(self) -> None:
        """Test that a reverse sorted list becomes sorted in ascending order."""
        lst: List[int] = [5, 4, 3, 2, 1]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3, 4, 5]

    def test_reverse_sorted_longer(self) -> None:
        """Test reverse sorted list of longer length."""
        lst: List[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_unsorted_list(self) -> None:
        """Test that an unsorted list is correctly sorted."""
        lst: List[int] = [5, 3, 2, 1, 4]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3, 4, 5]

    def test_unsorted_multiple_elements(self) -> None:
        """Test unsorted list with multiple elements."""
        lst: List[int] = [64, 34, 25, 12, 22, 11, 90]
        Sort.sort_list(lst)
        assert lst == [11, 12, 22, 25, 34, 64, 90]


class TestSortListDuplicates:
    """Test lists with duplicate values."""

    def test_all_duplicates(self) -> None:
        """Test that a list of all duplicate values remains unchanged."""
        lst: List[int] = [5, 5, 5, 5, 5]
        Sort.sort_list(lst)
        assert lst == [5, 5, 5, 5, 5]

    def test_some_duplicates(self) -> None:
        """Test that duplicates are handled correctly in sorting."""
        lst: List[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        Sort.sort_list(lst)
        assert lst == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_duplicates_at_end(self) -> None:
        """Test list with duplicates at the end."""
        lst: List[int] = [5, 4, 3, 2, 2, 2]
        Sort.sort_list(lst)
        assert lst == [2, 2, 2, 3, 4, 5]

    def test_duplicates_at_start(self) -> None:
        """Test list with duplicates at the start."""
        lst: List[int] = [3, 3, 3, 5, 4, 2]
        Sort.sort_list(lst)
        assert lst == [2, 3, 3, 3, 4, 5]

    def test_pairs_of_duplicates(self) -> None:
        """Test list with pairs of duplicate values."""
        lst: List[int] = [2, 2, 1, 1, 3, 3]
        Sort.sort_list(lst)
        assert lst == [1, 1, 2, 2, 3, 3]


class TestSortListNegativeNumbers:
    """Test lists with negative numbers."""

    def test_all_negative(self) -> None:
        """Test that all negative numbers are sorted correctly."""
        lst: List[int] = [-5, -3, -1, -2, -4]
        Sort.sort_list(lst)
        assert lst == [-5, -4, -3, -2, -1]

    def test_single_negative(self) -> None:
        """Test list with a single negative number."""
        lst: List[int] = [3, 1, -5, 2]
        Sort.sort_list(lst)
        assert lst == [-5, 1, 2, 3]

    def test_negative_sorted(self) -> None:
        """Test that already sorted negative numbers remain sorted."""
        lst: List[int] = [-10, -5, -3, -1]
        Sort.sort_list(lst)
        assert lst == [-10, -5, -3, -1]

    def test_negative_reverse_sorted(self) -> None:
        """Test that reverse sorted negative numbers are sorted correctly."""
        lst: List[int] = [-1, -3, -5, -10]
        Sort.sort_list(lst)
        assert lst == [-10, -5, -3, -1]


class TestSortListMixedValues:
    """Test lists with mixed positive and negative values."""

    def test_mixed_positive_negative(self) -> None:
        """Test list with mixed positive and negative values."""
        lst: List[int] = [3, -1, 4, -5, 2, -3]
        Sort.sort_list(lst)
        assert lst == [-5, -3, -1, 2, 3, 4]

    def test_mixed_with_zero(self) -> None:
        """Test list with zero and mixed positive/negative values."""
        lst: List[int] = [5, -3, 0, 2, -1, 0, 4]
        Sort.sort_list(lst)
        assert lst == [-3, -1, 0, 0, 2, 4, 5]

    def test_mixed_unsorted(self) -> None:
        """Test unsorted list with mixed values."""
        lst: List[int] = [-10, 50, -5, 30, 0, -20, 10]
        Sort.sort_list(lst)
        assert lst == [-20, -10, -5, 0, 10, 30, 50]

    def test_mixed_duplicates(self) -> None:
        """Test list with mixed values and duplicates."""
        lst: List[int] = [2, -2, 2, -2, 0, 1, -1]
        Sort.sort_list(lst)
        assert lst == [-2, -2, -1, 0, 1, 2, 2]


class TestSortListReturnValue:
    """Test return value behavior of Sort.sort_list()."""

    def test_returns_none(self) -> None:
        """Test that sort_list returns None (modifies in-place)."""
        lst: List[int] = [3, 1, 2]
        result = Sort.sort_list(lst)
        assert result is None

    def test_returns_none_empty(self) -> None:
        """Test that sort_list returns None for empty list."""
        lst: List[int] = []
        result = Sort.sort_list(lst)
        assert result is None

    def test_returns_none_single(self) -> None:
        """Test that sort_list returns None for single element."""
        lst: List[int] = [42]
        result = Sort.sort_list(lst)
        assert result is None


class TestSortListInPlaceModification:
    """Test that Sort.sort_list() modifies the list in-place."""

    def test_in_place_modification_original_reference(self) -> None:
        """Test that the original list object is modified, not replaced."""
        lst: List[int] = [3, 1, 2]
        original_id = id(lst)
        Sort.sort_list(lst)
        assert id(lst) == original_id
        assert lst == [1, 2, 3]

    def test_in_place_modification_list_changed(self) -> None:
        """Test that the original list contents are changed."""
        lst: List[int] = [5, 2, 8, 1, 9]
        Sort.sort_list(lst)
        assert lst == [1, 2, 5, 8, 9]
        assert isinstance(lst, list)

    def test_in_place_no_new_list_created(self) -> None:
        """Test that no new list is created; original is modified."""
        original_list = [4, 2, 7, 1]
        original_id = id(original_list)
        Sort.sort_list(original_list)
        # Verify the object identity hasn't changed
        assert id(original_list) == original_id
        assert original_list == [1, 2, 4, 7]

    def test_in_place_with_duplicates(self) -> None:
        """Test in-place modification with duplicates."""
        lst: List[int] = [3, 1, 3, 2, 1]
        original_id = id(lst)
        Sort.sort_list(lst)
        assert id(lst) == original_id
        assert lst == [1, 1, 2, 3, 3]

    def test_in_place_with_negative(self) -> None:
        """Test in-place modification with negative numbers."""
        lst: List[int] = [2, -3, 1, -1, 0]
        original_id = id(lst)
        Sort.sort_list(lst)
        assert id(lst) == original_id
        assert lst == [-3, -1, 0, 1, 2]


class TestSortListLargerLists:
    """Test Sort.sort_list() with larger datasets."""

    def test_larger_unsorted_list(self) -> None:
        """Test sorting a larger unsorted list."""
        lst: List[int] = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 43, 32, 19]
        Sort.sort_list(lst)
        assert lst == [11, 12, 19, 22, 25, 32, 34, 43, 50, 64, 76, 88, 90]

    def test_larger_reverse_sorted_list(self) -> None:
        """Test sorting a larger reverse sorted list."""
        lst: List[int] = list(range(100, 0, -1))
        Sort.sort_list(lst)
        assert lst == list(range(1, 101))

    def test_larger_random_like_list(self) -> None:
        """Test sorting a larger random-like list."""
        lst: List[int] = [42, 17, 93, 5, 38, 61, 29, 74, 11, 86, 
                         52, 8, 77, 31, 64, 45, 19, 82, 3, 98]
        Sort.sort_list(lst)
        assert lst == [3, 5, 8, 11, 17, 19, 29, 31, 38, 42, 45, 52, 61, 64, 74, 77, 82, 86, 93, 98]

    def test_larger_with_duplicates(self) -> None:
        """Test sorting a larger list with many duplicates."""
        lst: List[int] = [5, 2, 8, 2, 9, 1, 5, 3, 8, 2, 9, 1, 5]
        Sort.sort_list(lst)
        assert lst == [1, 1, 2, 2, 2, 3, 5, 5, 5, 8, 8, 9, 9]


class TestSortListEdgeCasesComprehensive:
    """Comprehensive edge cases for Sort.sort_list()."""

    def test_two_elements_unsorted(self) -> None:
        """Test two element list that needs sorting."""
        lst: List[int] = [2, 1]
        Sort.sort_list(lst)
        assert lst == [1, 2]

    def test_three_elements_pivot_middle(self) -> None:
        """Test three elements with middle element as pivot."""
        lst: List[int] = [3, 1, 2]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3]

    def test_identical_values_many(self) -> None:
        """Test list with many identical values."""
        lst: List[int] = [7] * 10
        Sort.sort_list(lst)
        assert lst == [7] * 10

    def test_two_unique_values_alternating(self) -> None:
        """Test list with two unique values alternating."""
        lst: List[int] = [1, 2, 1, 2, 1, 2, 1, 2]
        Sort.sort_list(lst)
        assert lst == [1, 1, 1, 1, 2, 2, 2, 2]

    def test_large_negative_and_positive(self) -> None:
        """Test with very large negative and positive numbers."""
        lst: List[int] = [1000000, -1000000, 0, 999999, -999999]
        Sort.sort_list(lst)
        assert lst == [-1000000, -999999, 0, 999999, 1000000]

    def test_single_swap_needed(self) -> None:
        """Test list where only one swap is needed."""
        lst: List[int] = [1, 3, 2]
        Sort.sort_list(lst)
        assert lst == [1, 2, 3]


def test_sort_list_maintains_all_elements() -> None:
    """Test that sorting doesn't lose or create any elements."""
    lst: List[int] = [9, 3, 7, 1, 5, 2, 8, 4, 6]
    original_length = len(lst)
    original_sum = sum(lst)
    original_elements = sorted(lst)
    
    Sort.sort_list(lst)
    
    assert len(lst) == original_length
    assert sum(lst) == original_sum
    assert lst == original_elements


def test_sort_list_idempotent() -> None:
    """Test that sorting an already sorted list doesn't change it."""
    lst: List[int] = [1, 2, 3, 4, 5]
    Sort.sort_list(lst)
    lst_copy = lst.copy()
    Sort.sort_list(lst)
    assert lst == lst_copy


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([5, 2, 8, 1], [1, 2, 5, 8]),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 3, 3], [3, 3, 3]),
        ([-5, -1, -3], [-5, -3, -1]),
        ([10, -10], [-10, 10]),
        ([0, 0, 0], [0, 0, 0]),
        ([100, 50, 75, 25], [25, 50, 75, 100]),
        ([], []),
        ([5, 4, 3, 2, 1, 0, -1, -2], [-2, -1, 0, 1, 2, 3, 4, 5]),
    ],
)
def test_sort_list_parametrized(input_list: List[int], expected: List[int]) -> None:
    """Parametrized test for various input cases."""
    Sort.sort_list(input_list)
    assert input_list == expected


def test_benchmark_sort_list_small(benchmark) -> None:
    """Benchmark Sort.sort_list() with small list."""
    test_list = [5, 3, 2, 1, 4]
    benchmark(Sort.sort_list, test_list)


def test_benchmark_sort_list_medium(benchmark) -> None:
    """Benchmark Sort.sort_list() with medium list."""
    test_list = list(range(50, 0, -1))
    benchmark(Sort.sort_list, test_list)
