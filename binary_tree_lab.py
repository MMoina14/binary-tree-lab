from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Return the maximum depth of a binary tree.

    Approach (recursive DFS):
      - Base case: if the node is None, we've gone past a leaf — return 0.
      - Recursive case: compute the depth of the left and right subtrees,
        then return the larger of the two plus 1 for the current node.

    Time:  O(n) — every node is visited once.
    Space: O(h) — call stack equals tree height h.
    """
    # Base case: empty node contributes no depth
    if root is None:
        return 0

    # Recursively find the depth of each subtree
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Add 1 for the current node on top of the deeper subtree
    return max(left_depth, right_depth) + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the Lowest Common Ancestor (LCA) of nodes p and q in a BST.

    Approach (BST property navigation):
      - If BOTH p and q are less than root, the LCA is in the left subtree.
      - If BOTH p and q are greater than root, the LCA is in the right subtree.
      - Otherwise, root is the split point — it is the LCA.
        (This also handles the case where p or q equals root.)

    Time:  O(h) — follows a single root-to-LCA path.
    Space: O(h) — call stack equals tree height h.
    """
    # Both nodes are smaller → LCA must be in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both nodes are larger → LCA must be in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Values straddle (or match) root — this node is the LCA
    return root