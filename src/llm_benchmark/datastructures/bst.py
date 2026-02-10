from typing import Optional, List, Any


class Node:
    """A node in the Binary Search Tree.
    
    Attributes:
        value: The value stored in this node
        left: Reference to the left child node (None if no left child)
        right: Reference to the right child node (None if no right child)
    """

    def __init__(self, value: Any) -> None:
        """Initialize a Node with a value and no children.
        
        Args:
            value: The value to store in this node
        """
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class Tree:
    """A Binary Search Tree implementation.
    
    Maintains BST invariant: for each node, all values in left subtree < node value < all values in right subtree.
    Tracks size (number of nodes) and height of the tree.
    """

    def __init__(self, values: Optional[List[Any]] = None) -> None:
        """Initialize a Tree with optional initial values.
        
        Args:
            values: Optional list of values to insert into the tree.
                   If None, creates an empty tree.
        """
        self._root: Optional[Node] = None
        self._size: int = 0
        self._height: int = -1  # height of empty tree is -1
        
        if values is not None:
            for value in values:
                self._insert_value(value)
    
    def _insert_value(self, value: Any) -> None:
        """Insert a value into the BST.
        
        Args:
            value: The value to insert
        """
        if self._root is None:
            self._root = Node(value)
            self._size = 1
            self._height = 0
        else:
            self._size += self._insert_recursive(self._root, value)
            self._height = self._calculate_height(self._root)
    
    def _insert_recursive(self, node: Node, value: Any) -> int:
        """Recursively insert a value into the tree.
        
        Args:
            node: Current node in the tree
            value: Value to insert
            
        Returns:
            1 if a new node was inserted, 0 if value already exists
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return 1
            else:
                return self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return 1
            else:
                return self._insert_recursive(node.right, value)
        else:
            # Duplicate value - don't insert
            return 0
    
    @property
    def root(self) -> Optional[Node]:
        """Get the root node of the tree (read-only).
        
        Returns:
            The root Node, or None if tree is empty
        """
        return self._root
    
    @property
    def size(self) -> int:
        """Get the number of nodes in the tree (read-only).
        
        Returns:
            The count of nodes in the tree
        """
        return self._size
    
    @property
    def height(self) -> int:
        """Get the height of the tree (read-only).
        
        Returns:
            The height of the tree (-1 for empty tree, 0 for single node, etc.)
        """
        return self._height
    
    def _is_valid_bst(self) -> bool:
        """Verify that the tree satisfies BST invariants.
        
        BST invariant: For each node, all values in the left subtree are less than
        the node's value, and all values in the right subtree are greater than
        the node's value.
        
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        def is_valid_bst_recursive(node: Optional[Node], min_value: Any = None, max_value: Any = None) -> bool:
            """Helper function to validate BST properties recursively.
            
            Args:
                node: Current node being validated
                min_value: Minimum value this node's value must exceed (or None)
                max_value: Maximum value this node's value must not exceed (or None)
                
            Returns:
                True if this subtree is a valid BST, False otherwise
            """
            if node is None:
                return True
            
            # Check if current node violates constraints
            if min_value is not None and node.value <= min_value:
                return False
            if max_value is not None and node.value >= max_value:
                return False
            
            # Recursively validate left and right subtrees
            return (is_valid_bst_recursive(node.left, min_value, node.value) and
                    is_valid_bst_recursive(node.right, node.value, max_value))
        
        return is_valid_bst_recursive(self._root)
    
    def _calculate_height(self, node: Optional[Node]) -> int:
        """Calculate the height of a subtree rooted at the given node.
        
        Height is defined as the number of edges from the node to the deepest leaf.
        Empty tree (None) has height -1.
        A single node has height 0.
        
        Args:
            node: The root of the subtree to measure
            
        Returns:
            The height of the subtree (-1 for None, 0 for leaf node, etc.)
        """
        if node is None:
            return -1
        
        left_height = self._calculate_height(node.left)
        right_height = self._calculate_height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def inorder_traversal(self) -> List[Any]:
        """Perform an inorder traversal of the tree.
        
        Inorder traversal visits nodes in sorted order (left subtree, node, right subtree).
        For a valid BST, this should return values in sorted (non-decreasing) order.
        
        Returns:
            A list of values in inorder sequence
        """
        result: List[Any] = []
        
        def inorder_recursive(node: Optional[Node]) -> None:
            """Helper function for recursive inorder traversal.
            
            Args:
                node: Current node being visited
            """
            if node is not None:
                inorder_recursive(node.left)
                result.append(node.value)
                inorder_recursive(node.right)
        
        inorder_recursive(self._root)
        return result


# Public module-level functions for BST operations

def bst_insert(tree: Tree, value: Any) -> Tree:
    """Insert a value into the Binary Search Tree.
    
    Adds the value to the tree while maintaining the BST property:
    - All values in the left subtree are less than the node's value
    - All values in the right subtree are greater than the node's value
    
    DUPLICATE HANDLING: Duplicates are REJECTED. If the value already exists
    in the tree, the insertion is ignored and the tree is returned unchanged.
    This decision was made to maintain O(log n) search performance and simplify
    the tree structure. Alternative approaches (allowing duplicates in right
    subtree or tracking counts) were considered but rejected for simplicity.
    
    Args:
        tree: The Tree to insert into
        value: The value to insert
        
    Returns:
        The modified tree (same reference)
        
    Raises:
        TypeError: If tree is not a Tree instance
        
    Example:
        >>> tree = Tree()
        >>> tree = bst_insert(tree, 5)
        >>> tree = bst_insert(tree, 3)
        >>> tree = bst_insert(tree, 7)
        >>> tree.size
        3
        >>> tree = bst_insert(tree, 5)  # Duplicate, ignored
        >>> tree.size
        3
    """
    if not isinstance(tree, Tree):
        raise TypeError(f"Expected Tree instance, got {type(tree).__name__}")
    
    tree._insert_value(value)
    return tree


def bst_search(tree: Tree, value: Any) -> bool:
    """Search for a value in the Binary Search Tree using recursion.
    
    Performs a recursive depth-first search to locate the target value.
    Time complexity: O(log n) average case (balanced tree), O(n) worst case (degenerate tree)
    Space complexity: O(log n) average case (call stack), O(n) worst case
    
    Args:
        tree: The Tree to search in
        value: The value to search for
        
    Returns:
        True if the value is found in the tree, False otherwise
        
    Raises:
        TypeError: If tree is not a Tree instance
        
    Example:
        >>> tree = Tree([5, 3, 7, 1, 9])
        >>> bst_search(tree, 7)
        True
        >>> bst_search(tree, 10)
        False
    """
    if not isinstance(tree, Tree):
        raise TypeError(f"Expected Tree instance, got {type(tree).__name__}")
    
    def search_recursive(node: Optional[Node], target: Any) -> bool:
        """Recursively search for a value in the tree.
        
        Args:
            node: Current node being examined
            target: The value to search for
            
        Returns:
            True if target is found in the subtree, False otherwise
        """
        if node is None:
            return False
        
        if target == node.value:
            return True
        elif target < node.value:
            return search_recursive(node.left, target)
        else:
            return search_recursive(node.right, target)
    
    return search_recursive(tree.root, value)


def bst_search_iterative(tree: Tree, value: Any) -> bool:
    """Search for a value in the Binary Search Tree using iteration.
    
    Performs an iterative depth-first search to locate the target value.
    This approach avoids the call stack overhead of recursion.
    Time complexity: O(log n) average case (balanced tree), O(n) worst case (degenerate tree)
    Space complexity: O(1) - constant space, no call stack
    
    Args:
        tree: The Tree to search in
        value: The value to search for
        
    Returns:
        True if the value is found in the tree, False otherwise
        
    Raises:
        TypeError: If tree is not a Tree instance
        
    Example:
        >>> tree = Tree([5, 3, 7, 1, 9])
        >>> bst_search_iterative(tree, 7)
        True
        >>> bst_search_iterative(tree, 10)
        False
    """
    if not isinstance(tree, Tree):
        raise TypeError(f"Expected Tree instance, got {type(tree).__name__}")
    
    current = tree.root
    
    while current is not None:
        if value == current.value:
            return True
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    
    return False
