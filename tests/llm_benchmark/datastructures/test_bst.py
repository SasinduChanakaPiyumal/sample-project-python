"""Comprehensive unit tests for Binary Search Tree implementation.

Tests cover:
- Basic insertion and search operations
- Edge cases (empty tree, single element, duplicates)
- BST invariant validation through inorder traversal
- Both recursive and iterative search implementations
- Small (10 elements) and medium (100 elements) datasets
"""

import pytest
from src.llm_benchmark.datastructures.bst import (
    Tree, Node, bst_insert, bst_search, bst_search_iterative
)


class TestTreeBasics:
    """Test basic Tree class initialization and properties."""
    
    def test_empty_tree_initialization(self):
        """Test creation of an empty tree."""
        tree = Tree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.height == -1
    
    def test_tree_with_single_value(self):
        """Test creating a tree with a single initial value."""
        tree = Tree([5])
        assert tree.root is not None
        assert tree.root.value == 5
        assert tree.size == 1
        assert tree.height == 0
    
    def test_tree_initialization_with_multiple_values(self):
        """Test creating a tree with multiple initial values."""
        values = [5, 3, 7, 1, 9]
        tree = Tree(values)
        assert tree.size == 5
        assert tree.root.value == 5
        assert tree._is_valid_bst() is True


class TestBstInsert:
    """Test bst_insert() function."""
    
    def test_insert_into_empty_tree(self):
        """Test inserting into an empty tree."""
        tree = Tree()
        tree = bst_insert(tree, 5)
        
        assert tree.size == 1
        assert tree.root is not None
        assert tree.root.value == 5
        assert tree.height == 0
    
    def test_insert_multiple_values(self):
        """Test inserting multiple values maintains BST property."""
        tree = Tree()
        values = [5, 3, 7, 1, 9, 4, 6]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == len(values)
        assert tree._is_valid_bst() is True
    
    def test_insert_left_subtree(self):
        """Test that smaller values go to left subtree."""
        tree = Tree([5])
        tree = bst_insert(tree, 3)
        
        assert tree.root.left is not None
        assert tree.root.left.value == 3
        assert tree.root.right is None
    
    def test_insert_right_subtree(self):
        """Test that larger values go to right subtree."""
        tree = Tree([5])
        tree = bst_insert(tree, 7)
        
        assert tree.root.right is not None
        assert tree.root.right.value == 7
        assert tree.root.left is None
    
    def test_insert_duplicate_rejected(self):
        """Test that duplicate values are rejected."""
        tree = Tree([5, 3, 7])
        initial_size = tree.size
        
        tree = bst_insert(tree, 5)
        assert tree.size == initial_size  # Size unchanged
        
        tree = bst_insert(tree, 3)
        assert tree.size == initial_size  # Size unchanged
        
        tree = bst_insert(tree, 7)
        assert tree.size == initial_size  # Size unchanged
    
    def test_insert_maintains_bst_property(self):
        """Test that insertion maintains BST invariant."""
        tree = Tree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
        
        for value in values:
            tree = bst_insert(tree, value)
            # Verify BST property after each insertion
            assert tree._is_valid_bst() is True
    
    def test_insert_type_validation(self):
        """Test that invalid tree type raises TypeError."""
        with pytest.raises(TypeError):
            bst_insert("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_insert(None, 5)
        
        with pytest.raises(TypeError):
            bst_insert([], 5)
    
    def test_insert_negative_numbers(self):
        """Test insertion of negative numbers."""
        tree = Tree([0, -5, 5, -3, -10, 3, 10])
        assert tree.size == 7
        assert tree._is_valid_bst() is True
    
    def test_insert_floating_point(self):
        """Test insertion of floating point numbers."""
        tree = Tree([5.5, 3.3, 7.7, 1.1, 9.9])
        assert tree.size == 5
        assert tree._is_valid_bst() is True
    
    def test_insert_strings(self):
        """Test insertion of string values."""
        tree = Tree(['dog', 'cat', 'elephant', 'ant', 'zebra'])
        assert tree.size == 5
        assert tree._is_valid_bst() is True


class TestBstSearch:
    """Test bst_search() recursive function."""
    
    def test_search_empty_tree(self):
        """Test searching in an empty tree."""
        tree = Tree()
        assert bst_search(tree, 5) is False
    
    def test_search_existing_root(self):
        """Test searching for the root value."""
        tree = Tree([5])
        assert bst_search(tree, 5) is True
    
    def test_search_existing_left_child(self):
        """Test searching for a value in left subtree."""
        tree = Tree([5, 3, 7])
        assert bst_search(tree, 3) is True
    
    def test_search_existing_right_child(self):
        """Test searching for a value in right subtree."""
        tree = Tree([5, 3, 7])
        assert bst_search(tree, 7) is True
    
    def test_search_nonexistent_value(self):
        """Test searching for a value not in tree."""
        tree = Tree([5, 3, 7, 1, 9])
        assert bst_search(tree, 10) is False
        assert bst_search(tree, 0) is False
        assert bst_search(tree, 6) is False
    
    def test_search_multiple_levels(self):
        """Test searching at various depths in tree."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search(tree, value) is True
    
    def test_search_not_found(self):
        """Test searching for values not in tree."""
        tree = Tree([50, 30, 70, 20, 40, 60, 80])
        
        not_found = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
        for value in not_found:
            assert bst_search(tree, value) is False
    
    def test_search_type_validation(self):
        """Test that invalid tree type raises TypeError."""
        with pytest.raises(TypeError):
            bst_search("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_search(None, 5)
        
        with pytest.raises(TypeError):
            bst_search([], 5)


class TestBstSearchIterative:
    """Test bst_search_iterative() function."""
    
    def test_search_iterative_empty_tree(self):
        """Test iterative search in an empty tree."""
        tree = Tree()
        assert bst_search_iterative(tree, 5) is False
    
    def test_search_iterative_existing_root(self):
        """Test iterative search for the root value."""
        tree = Tree([5])
        assert bst_search_iterative(tree, 5) is True
    
    def test_search_iterative_existing_left_child(self):
        """Test iterative search for a value in left subtree."""
        tree = Tree([5, 3, 7])
        assert bst_search_iterative(tree, 3) is True
    
    def test_search_iterative_existing_right_child(self):
        """Test iterative search for a value in right subtree."""
        tree = Tree([5, 3, 7])
        assert bst_search_iterative(tree, 7) is True
    
    def test_search_iterative_nonexistent_value(self):
        """Test iterative search for a value not in tree."""
        tree = Tree([5, 3, 7, 1, 9])
        assert bst_search_iterative(tree, 10) is False
        assert bst_search_iterative(tree, 0) is False
        assert bst_search_iterative(tree, 6) is False
    
    def test_search_iterative_multiple_levels(self):
        """Test iterative search at various depths in tree."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search_iterative(tree, value) is True
    
    def test_search_iterative_not_found(self):
        """Test iterative search for values not in tree."""
        tree = Tree([50, 30, 70, 20, 40, 60, 80])
        
        not_found = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
        for value in not_found:
            assert bst_search_iterative(tree, value) is False
    
    def test_search_iterative_type_validation(self):
        """Test that invalid tree type raises TypeError."""
        with pytest.raises(TypeError):
            bst_search_iterative("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_search_iterative(None, 5)
        
        with pytest.raises(TypeError):
            bst_search_iterative([], 5)
    
    def test_search_recursive_vs_iterative_equivalence(self):
        """Test that recursive and iterative search produce same results."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # Test finding values
        for value in values:
            recursive_result = bst_search(tree, value)
            iterative_result = bst_search_iterative(tree, value)
            assert recursive_result == iterative_result == True
        
        # Test not finding values
        not_found = [5, 15, 27, 42, 55, 72, 90]
        for value in not_found:
            recursive_result = bst_search(tree, value)
            iterative_result = bst_search_iterative(tree, value)
            assert recursive_result == iterative_result == False


class TestBstInorderTraversal:
    """Test inorder traversal and BST property validation."""
    
    def test_inorder_empty_tree(self):
        """Test inorder traversal of empty tree."""
        tree = Tree()
        result = tree.inorder_traversal()
        assert result == []
    
    def test_inorder_single_node(self):
        """Test inorder traversal of single node."""
        tree = Tree([5])
        result = tree.inorder_traversal()
        assert result == [5]
    
    def test_inorder_yields_sorted_sequence(self):
        """Test that inorder traversal yields sorted sequence."""
        values = [5, 3, 7, 1, 9, 4, 6, 8, 2]
        tree = Tree(values)
        result = tree.inorder_traversal()
        
        # Inorder should yield values in sorted order
        assert result == sorted(values)
    
    def test_inorder_maintains_order_after_insertion(self):
        """Test inorder traversal remains sorted after insertions."""
        tree = Tree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        
        for value in values:
            tree = bst_insert(tree, value)
            result = tree.inorder_traversal()
            # After each insertion, inorder should be sorted
            assert result == sorted(result)
    
    def test_inorder_with_duplicates_attempted(self):
        """Test inorder traversal when duplicates are attempted."""
        tree = Tree([5, 3, 7])
        tree = bst_insert(tree, 5)  # Attempt duplicate
        tree = bst_insert(tree, 3)  # Attempt duplicate
        
        result = tree.inorder_traversal()
        assert result == [3, 5, 7]  # Duplicates not added


class TestSmallDataset:
    """Test with small dataset (10 elements) for correctness."""
    
    def test_insertion_correctness_10_elements(self):
        """Test insertion correctness with 10 elements."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        tree = Tree(values)
        
        assert tree.size == 10
        assert tree._is_valid_bst() is True
        assert tree.inorder_traversal() == sorted(values)
    
    def test_search_correctness_10_elements(self):
        """Test search correctness with 10 elements."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search(tree, value) is True
            assert bst_search_iterative(tree, value) is True
        
        # Non-existent values should not be found
        not_in_tree = [5, 15, 45, 55, 65, 75, 85, 95, 100]
        for value in not_in_tree:
            assert bst_search(tree, value) is False
            assert bst_search_iterative(tree, value) is False
    
    def test_height_with_10_elements(self):
        """Test height calculation with 10 elements."""
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        tree = Tree(values)
        # Tree is reasonably balanced, height should be around 3
        assert tree.height >= 2
        assert tree.height <= 4


class TestMediumDataset:
    """Test with medium dataset (100 elements) for correctness."""
    
    def test_insertion_correctness_100_elements(self):
        """Test insertion correctness with 100 elements."""
        values = list(range(100, 0, -1))  # 100, 99, 98, ..., 1 (worst case ordering)
        tree = Tree(values)
        
        assert tree.size == 100
        assert tree._is_valid_bst() is True
        assert tree.inorder_traversal() == sorted(values)
    
    def test_search_correctness_100_elements(self):
        """Test search correctness with 100 elements."""
        values = list(range(1, 101))
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search(tree, value) is True
            assert bst_search_iterative(tree, value) is True
        
        # Some non-existent values should not be found
        not_in_tree = [0, 101, 150, 200]
        for value in not_in_tree:
            assert bst_search(tree, value) is False
            assert bst_search_iterative(tree, value) is False
    
    def test_insertion_and_search_interleaved_100_elements(self):
        """Test interleaved insertion and search with 100 elements."""
        tree = Tree()
        values = list(range(50, -50, -1))  # 50, 49, ..., -49
        
        # Insert first 50 values
        for value in values[:50]:
            tree = bst_insert(tree, value)
        
        # Search for some inserted values
        for value in values[:25]:
            assert bst_search(tree, value) is True
        
        # Insert remaining values
        for value in values[50:]:
            tree = bst_insert(tree, value)
        
        # Search for all values
        for value in values:
            assert bst_search_iterative(tree, value) is True
        
        # Verify BST property and sorted order
        assert tree.inorder_traversal() == sorted(values)


class TestEdgeCases:
    """Test edge cases and corner scenarios."""
    
    def test_insert_and_search_single_element(self):
        """Test insertion and search with single element."""
        tree = Tree()
        tree = bst_insert(tree, 42)
        
        assert bst_search(tree, 42) is True
        assert bst_search_iterative(tree, 42) is True
        assert bst_search(tree, 41) is False
        assert bst_search_iterative(tree, 41) is False
    
    def test_insert_ascending_order(self):
        """Test insertion in ascending order (creates right-skewed tree)."""
        tree = Tree()
        values = [1, 2, 3, 4, 5]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == 5
        assert tree.inorder_traversal() == values
        assert tree._is_valid_bst() is True
    
    def test_insert_descending_order(self):
        """Test insertion in descending order (creates left-skewed tree)."""
        tree = Tree()
        values = [5, 4, 3, 2, 1]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == 5
        assert tree.inorder_traversal() == sorted(values)
        assert tree._is_valid_bst() is True
    
    def test_insert_zero_and_negative(self):
        """Test insertion of zero and negative numbers."""
        tree = Tree([0, -5, 5, -10, 10])
        
        assert bst_search(tree, 0) is True
        assert bst_search(tree, -5) is True
        assert bst_search(tree, -10) is True
        assert bst_search_iterative(tree, -5) is True
        assert tree._is_valid_bst() is True
    
    def test_search_boundary_values(self):
        """Test search with boundary values."""
        tree = Tree([50, 25, 75, 10, 30, 60, 90])
        
        # Search for min value
        assert bst_search(tree, 10) is True
        # Search for max value
        assert bst_search(tree, 90) is True
        # Search just below min
        assert bst_search(tree, 9) is False
        # Search just above max
        assert bst_search(tree, 91) is False
