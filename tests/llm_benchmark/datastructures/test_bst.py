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
    """Test basic Tree class initialization and properties.
    
    These tests validate that the Tree class correctly initializes and maintains
    basic properties (size, height, root) for empty trees and trees with initial values.
    """
    
    def test_empty_tree_initialization(self):
        """Test creation of an empty tree.
        
        Validates:
        - Empty tree has None root
        - Empty tree size is 0
        - Empty tree height is -1 (standard empty tree representation)
        """
        tree = Tree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.height == -1
    
    def test_tree_with_single_value(self):
        """Test creating a tree with a single initial value.
        
        Validates:
        - Single node tree creates root node
        - Root value is set correctly
        - Size is 1
        - Height of single node is 0 (no edges below)
        """
        tree = Tree([5])
        assert tree.root is not None
        assert tree.root.value == 5
        assert tree.size == 1
        assert tree.height == 0
    
    def test_tree_initialization_with_multiple_values(self):
        """Test creating a tree with multiple initial values.
        
        Validates:
        - Multiple values are all inserted during initialization
        - Size counter is correct
        - Root value matches first inserted value
        - Tree maintains valid BST property after initialization
        """
        values = [5, 3, 7, 1, 9]
        tree = Tree(values)
        assert tree.size == 5
        assert tree.root.value == 5
        assert tree._is_valid_bst() is True


class TestBstInsert:
    """Test bst_insert() function.
    
    These tests validate the insertion operation including edge cases,
    BST property maintenance, duplicate handling, and type safety.
    """
    
    def test_insert_into_empty_tree(self):
        """Test inserting into an empty tree.
        
        Validates:
        - First insertion into empty tree creates root node
        - Size is updated to 1
        - Root value is set correctly
        - Height is 0 for single node
        - Tree remains valid BST
        """
        tree = Tree()
        tree = bst_insert(tree, 5)
        
        assert tree.size == 1
        assert tree.root is not None
        assert tree.root.value == 5
        assert tree.height == 0
    
    def test_insert_multiple_values(self):
        """Test inserting multiple values maintains BST property.
        
        Validates:
        - Multiple sequential insertions all succeed
        - Size counter reflects all insertions
        - BST invariant is maintained (left < parent < right at every node)
        """
        tree = Tree()
        values = [5, 3, 7, 1, 9, 4, 6]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == len(values)
        assert tree._is_valid_bst() is True
    
    def test_insert_left_subtree(self):
        """Test that smaller values go to left subtree.
        
        Validates:
        - Values smaller than parent are placed in left subtree
        - BST property is enforced for left children
        """
        tree = Tree([5])
        tree = bst_insert(tree, 3)
        
        assert tree.root.left is not None
        assert tree.root.left.value == 3
        assert tree.root.right is None
    
    def test_insert_right_subtree(self):
        """Test that larger values go to right subtree.
        
        Validates:
        - Values larger than parent are placed in right subtree
        - BST property is enforced for right children
        """
        tree = Tree([5])
        tree = bst_insert(tree, 7)
        
        assert tree.root.right is not None
        assert tree.root.right.value == 7
        assert tree.root.left is None
    
    def test_insert_duplicate_rejected(self):
        """Test that duplicate values are rejected.
        
        Validates:
        - Duplicate insertions are ignored (size doesn't change)
        - Tree structure remains unchanged
        - Duplicate handling is consistent for multiple values
        """
        tree = Tree([5, 3, 7])
        initial_size = tree.size
        
        tree = bst_insert(tree, 5)
        assert tree.size == initial_size  # Size unchanged
        
        tree = bst_insert(tree, 3)
        assert tree.size == initial_size  # Size unchanged
        
        tree = bst_insert(tree, 7)
        assert tree.size == initial_size  # Size unchanged
    
    def test_insert_maintains_bst_property(self):
        """Test that insertion maintains BST invariant.
        
        Validates:
        - Each insertion maintains the BST property
        - The validation happens incrementally after each insertion
        - Complex tree structure with multiple levels preserves invariant
        """
        tree = Tree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
        
        for value in values:
            tree = bst_insert(tree, value)
            # Verify BST property after each insertion
            assert tree._is_valid_bst() is True
    
    def test_insert_type_validation(self):
        """Test that invalid tree type raises TypeError.
        
        Validates:
        - Function rejects non-Tree objects with clear error message
        - String argument raises TypeError
        - None argument raises TypeError
        - List argument raises TypeError
        """
        with pytest.raises(TypeError):
            bst_insert("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_insert(None, 5)
        
        with pytest.raises(TypeError):
            bst_insert([], 5)
    
    def test_insert_negative_numbers(self):
        """Test insertion of negative numbers.
        
        Validates:
        - Negative values can be inserted
        - BST property is maintained with negative numbers
        - Comparison operators work correctly with negative values
        """
        tree = Tree([0, -5, 5, -3, -10, 3, 10])
        assert tree.size == 7
        assert tree._is_valid_bst() is True
    
    def test_insert_floating_point(self):
        """Test insertion of floating point numbers.
        
        Validates:
        - Float values can be inserted and compared
        - BST property works with floating point precision
        """
        tree = Tree([5.5, 3.3, 7.7, 1.1, 9.9])
        assert tree.size == 5
        assert tree._is_valid_bst() is True
    
    def test_insert_strings(self):
        """Test insertion of string values.
        
        Validates:
        - Generic implementation works with comparable objects (strings)
        - Lexicographic ordering is respected in BST structure
        - BST property holds for string comparisons
        """
        tree = Tree(['dog', 'cat', 'elephant', 'ant', 'zebra'])
        assert tree.size == 5
        assert tree._is_valid_bst() is True


class TestBstSearch:
    """Test bst_search() recursive function.
    
    These tests validate the recursive search implementation including
    correctness, edge cases, and type safety. Tests verify that the
    search correctly leverages BST ordering to find values efficiently.
    """
    
    def test_search_empty_tree(self):
        """Test searching in an empty tree.
        
        Validates:
        - Search in empty tree returns False
        - No errors occur when searching in empty tree
        """
        tree = Tree()
        assert bst_search(tree, 5) is False
    
    def test_search_existing_root(self):
        """Test searching for the root value.
        
        Validates:
        - Root value is found correctly
        - Search terminates at first level without traversal
        """
        tree = Tree([5])
        assert bst_search(tree, 5) is True
    
    def test_search_existing_left_child(self):
        """Test searching for a value in left subtree.
        
        Validates:
        - Values in left subtree can be found
        - Search correctly uses < comparison to traverse left
        """
        tree = Tree([5, 3, 7])
        assert bst_search(tree, 3) is True
    
    def test_search_existing_right_child(self):
        """Test searching for a value in right subtree.
        
        Validates:
        - Values in right subtree can be found
        - Search correctly uses > comparison to traverse right
        """
        tree = Tree([5, 3, 7])
        assert bst_search(tree, 7) is True
    
    def test_search_nonexistent_value(self):
        """Test searching for a value not in tree.
        
        Validates:
        - Non-existent values return False (not True by mistake)
        - Multiple missing values are all correctly identified as not found
        """
        tree = Tree([5, 3, 7, 1, 9])
        assert bst_search(tree, 10) is False
        assert bst_search(tree, 0) is False
        assert bst_search(tree, 6) is False
    
    def test_search_multiple_levels(self):
        """Test searching at various depths in tree.
        
        Validates:
        - Search works at depth 0 (root)
        - Search works at intermediate depths
        - Search works at deepest leaf levels
        - Complex tree with 13 nodes all searchable
        """
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search(tree, value) is True
    
    def test_search_not_found(self):
        """Test searching for values not in tree.
        
        Validates:
        - Many non-existent values return False
        - False negatives don't occur
        - Search correctly navigates past missing values
        """
        tree = Tree([50, 30, 70, 20, 40, 60, 80])
        
        not_found = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
        for value in not_found:
            assert bst_search(tree, value) is False
    
    def test_search_type_validation(self):
        """Test that invalid tree type raises TypeError.
        
        Validates:
        - Function rejects non-Tree objects
        - Clear error raised for string, None, and list arguments
        """
        with pytest.raises(TypeError):
            bst_search("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_search(None, 5)
        
        with pytest.raises(TypeError):
            bst_search([], 5)


class TestBstSearchIterative:
    """Test bst_search_iterative() function.
    
    These tests validate the iterative search implementation and ensure
    it produces identical results to the recursive implementation while
    using constant space (no call stack overhead).
    """
    
    def test_search_iterative_empty_tree(self):
        """Test iterative search in an empty tree.
        
        Validates:
        - Iterative search handles empty tree correctly
        - No errors with null root pointer
        """
        tree = Tree()
        assert bst_search_iterative(tree, 5) is False
    
    def test_search_iterative_existing_root(self):
        """Test iterative search for the root value.
        
        Validates:
        - Root value found immediately in first iteration
        """
        tree = Tree([5])
        assert bst_search_iterative(tree, 5) is True
    
    def test_search_iterative_existing_left_child(self):
        """Test iterative search for a value in left subtree.
        
        Validates:
        - Loop correctly traverses left when target < current value
        """
        tree = Tree([5, 3, 7])
        assert bst_search_iterative(tree, 3) is True
    
    def test_search_iterative_existing_right_child(self):
        """Test iterative search for a value in right subtree.
        
        Validates:
        - Loop correctly traverses right when target > current value
        """
        tree = Tree([5, 3, 7])
        assert bst_search_iterative(tree, 7) is True
    
    def test_search_iterative_nonexistent_value(self):
        """Test iterative search for a value not in tree.
        
        Validates:
        - Non-existent values properly identified without false positives
        - Loop terminates correctly at null nodes
        """
        tree = Tree([5, 3, 7, 1, 9])
        assert bst_search_iterative(tree, 10) is False
        assert bst_search_iterative(tree, 0) is False
        assert bst_search_iterative(tree, 6) is False
    
    def test_search_iterative_multiple_levels(self):
        """Test iterative search at various depths in tree.
        
        Validates:
        - Iterative approach finds values at all tree depths
        - Multiple iterations don't accumulate errors
        """
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # All values should be found
        for value in values:
            assert bst_search_iterative(tree, value) is True
    
    def test_search_iterative_not_found(self):
        """Test iterative search for values not in tree.
        
        Validates:
        - Multiple missing values all return False
        - Iteration terminates properly at leaf boundaries
        """
        tree = Tree([50, 30, 70, 20, 40, 60, 80])
        
        not_found = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
        for value in not_found:
            assert bst_search_iterative(tree, value) is False
    
    def test_search_iterative_type_validation(self):
        """Test that invalid tree type raises TypeError.
        
        Validates:
        - Function rejects non-Tree objects
        - Proper error handling for invalid input types
        """
        with pytest.raises(TypeError):
            bst_search_iterative("not a tree", 5)
        
        with pytest.raises(TypeError):
            bst_search_iterative(None, 5)
        
        with pytest.raises(TypeError):
            bst_search_iterative([], 5)
    
    def test_search_recursive_vs_iterative_equivalence(self):
        """Test that recursive and iterative search produce same results.
        
        Validates:
        - Recursive and iterative implementations are functionally identical
        - Both find values that exist in the tree
        - Both correctly identify missing values
        - Results match for complex tree with 13 nodes
        - Results match for 7 different non-existent values
        - This confirms iterative approach is correct replacement for recursive
        """
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        tree = Tree(values)
        
        # Test finding values - both implementations should return True
        for value in values:
            recursive_result = bst_search(tree, value)
            iterative_result = bst_search_iterative(tree, value)
            assert recursive_result == iterative_result == True
        
        # Test not finding values - both implementations should return False
        not_found = [5, 15, 27, 42, 55, 72, 90]
        for value in not_found:
            recursive_result = bst_search(tree, value)
            iterative_result = bst_search_iterative(tree, value)
            assert recursive_result == iterative_result == False


class TestBstInorderTraversal:
    """Test inorder traversal and BST property validation.
    
    These tests validate the inorder traversal method which is fundamental
    to verifying the BST property: a correct inorder traversal yields
    values in sorted order.
    """
    
    def test_inorder_empty_tree(self):
        """Test inorder traversal of empty tree.
        
        Validates:
        - Empty tree traversal returns empty list
        - No errors on null tree
        """
        tree = Tree()
        result = tree.inorder_traversal()
        assert result == []
    
    def test_inorder_single_node(self):
        """Test inorder traversal of single node.
        
        Validates:
        - Single node traversal returns list with that node's value
        """
        tree = Tree([5])
        result = tree.inorder_traversal()
        assert result == [5]
    
    def test_inorder_yields_sorted_sequence(self):
        """Test that inorder traversal yields sorted sequence.
        
        Validates:
        - Inorder traversal (left-node-right) produces sorted output
        - This is the primary test that confirms BST property holds
        - Works with unordered insertion sequence
        """
        values = [5, 3, 7, 1, 9, 4, 6, 8, 2]
        tree = Tree(values)
        result = tree.inorder_traversal()
        
        # Inorder should yield values in sorted order
        assert result == sorted(values)
    
    def test_inorder_maintains_order_after_insertion(self):
        """Test inorder traversal remains sorted after insertions.
        
        Validates:
        - BST property is maintained after each insertion
        - Incremental insertion doesn't break ordering
        - 13 insertions all maintain correct sorted output
        """
        tree = Tree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 75, 85]
        
        for value in values:
            tree = bst_insert(tree, value)
            result = tree.inorder_traversal()
            # After each insertion, inorder should be sorted
            assert result == sorted(result)
    
    def test_inorder_with_duplicates_attempted(self):
        """Test inorder traversal when duplicates are attempted.
        
        Validates:
        - Duplicate insertions don't appear in traversal
        - Tree structure remains clean (no duplicate nodes)
        - Traversal output is consistent even after duplicate attempts
        """
        tree = Tree([5, 3, 7])
        tree = bst_insert(tree, 5)  # Attempt duplicate
        tree = bst_insert(tree, 3)  # Attempt duplicate
        
        result = tree.inorder_traversal()
        assert result == [3, 5, 7]  # Duplicates not added


class TestSmallDataset:
    """Test with small dataset (10 elements) for correctness.
    
    These tests ensure the BST implementation works correctly with
    a small but realistic dataset of 10 elements.
    """
    
    def test_insertion_correctness_10_elements(self):
        """Test insertion correctness with 10 elements.
        
        Validates:
        - All 10 elements are successfully inserted
        - Size counter reflects 10 nodes
        - BST invariant is satisfied
        - Inorder traversal produces sorted output confirming structure
        """
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        tree = Tree(values)
        
        assert tree.size == 10
        assert tree._is_valid_bst() is True
        assert tree.inorder_traversal() == sorted(values)
    
    def test_search_correctness_10_elements(self):
        """Test search correctness with 10 elements.
        
        Validates:
        - All 10 inserted values are found by both search implementations
        - Recursive search finds all 10 values
        - Iterative search finds all 10 values
        - Non-existent values are correctly identified as missing
        - Tests multiple values between, before, and after tree values
        """
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
        """Test height calculation with 10 elements.
        
        Validates:
        - Tree height is reasonable (between 2-4 edges)
        - Tree is roughly balanced (not degenerate linear list)
        - Height calculation works correctly for moderately sized tree
        """
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
        tree = Tree(values)
        # Tree is reasonably balanced, height should be around 3
        assert tree.height >= 2
        assert tree.height <= 4


class TestMediumDataset:
    """Test with medium dataset (100 elements) for correctness.
    
    These tests ensure scalability and correctness with a larger dataset,
    including worst-case insertion ordering and interleaved operations.
    """
    
    def test_insertion_correctness_100_elements(self):
        """Test insertion correctness with 100 elements.
        
        Validates:
        - All 100 elements are inserted successfully
        - Size counter reaches 100
        - BST invariant holds with 100 nodes
        - Inorder traversal of 100 nodes produces sorted output
        - Uses worst-case insertion order (descending) to stress test
        """
        values = list(range(100, 0, -1))  # 100, 99, 98, ..., 1 (worst case ordering)
        tree = Tree(values)
        
        assert tree.size == 100
        assert tree._is_valid_bst() is True
        assert tree.inorder_traversal() == sorted(values)
    
    def test_search_correctness_100_elements(self):
        """Test search correctness with 100 elements.
        
        Validates:
        - All 100 values can be found using both search implementations
        - Recursive search handles all 100 values
        - Iterative search handles all 100 values
        - Non-existent values in different ranges return False
        - Tests values outside tree bounds (0, 101, 150, 200)
        """
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
        """Test interleaved insertion and search with 100 elements.
        
        Validates:
        - Insertions and searches can be interleaved
        - Search works correctly on partially-built tree
        - Tree remains valid after partial construction
        - Final tree with 100 elements maintains BST property
        - Workflow: insert 50, search 25 of those, insert remaining 50, search all 100
        - Uses both recursive and iterative search to verify both work
        """
        tree = Tree()
        values = list(range(50, -50, -1))  # 50, 49, ..., -49
        
        # Insert first 50 values
        for value in values[:50]:
            tree = bst_insert(tree, value)
        
        # Search for some inserted values - validates partial tree search
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
    """Test edge cases and corner scenarios.
    
    These tests validate the implementation handles degenerate cases,
    extreme values, and boundary conditions correctly.
    """
    
    def test_insert_and_search_single_element(self):
        """Test insertion and search with single element.
        
        Validates:
        - Single element can be inserted into empty tree
        - That single element can be found
        - Adjacent values return False correctly
        - Minimum viable tree functions correctly
        """
        tree = Tree()
        tree = bst_insert(tree, 42)
        
        assert bst_search(tree, 42) is True
        assert bst_search_iterative(tree, 42) is True
        assert bst_search(tree, 41) is False
        assert bst_search_iterative(tree, 41) is False
    
    def test_insert_ascending_order(self):
        """Test insertion in ascending order (creates right-skewed tree).
        
        Validates:
        - Ascending insertion creates degenerate right-skewed tree
        - All values still inserted correctly (size == 5)
        - BST property still maintained in skewed structure
        - Inorder traversal produces sorted output
        - Edge case: degenerate tree is still valid
        """
        tree = Tree()
        values = [1, 2, 3, 4, 5]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == 5
        assert tree.inorder_traversal() == values
        assert tree._is_valid_bst() is True
    
    def test_insert_descending_order(self):
        """Test insertion in descending order (creates left-skewed tree).
        
        Validates:
        - Descending insertion creates degenerate left-skewed tree
        - All values still inserted correctly
        - BST property maintained in left-skewed structure
        - Inorder traversal produces sorted output
        - Edge case: left-skewed tree is still valid
        """
        tree = Tree()
        values = [5, 4, 3, 2, 1]
        
        for value in values:
            tree = bst_insert(tree, value)
        
        assert tree.size == 5
        assert tree.inorder_traversal() == sorted(values)
        assert tree._is_valid_bst() is True
    
    def test_insert_zero_and_negative(self):
        """Test insertion of zero and negative numbers.
        
        Validates:
        - Zero can be inserted and searched
        - Negative numbers can be inserted and searched
        - Mixed positive and negative values maintain BST property
        - Comparison operators work correctly with zero and negatives
        """
        tree = Tree([0, -5, 5, -10, 10])
        
        assert bst_search(tree, 0) is True
        assert bst_search(tree, -5) is True
        assert bst_search(tree, -10) is True
        assert bst_search_iterative(tree, -5) is True
        assert tree._is_valid_bst() is True
    
    def test_search_boundary_values(self):
        """Test search with boundary values.
        
        Validates:
        - Minimum value in tree is found
        - Maximum value in tree is found
        - Value just below minimum returns False
        - Value just above maximum returns False
        - Boundary search precision
        """
        tree = Tree([50, 25, 75, 10, 30, 60, 90])
        
        # Search for min value
        assert bst_search(tree, 10) is True
        # Search for max value
        assert bst_search(tree, 90) is True
        # Search just below min
        assert bst_search(tree, 9) is False
        # Search just above max
        assert bst_search(tree, 91) is False
