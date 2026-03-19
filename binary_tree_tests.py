import unittest
from binary_tree_lab import TreeNode, max_depth, lowest_common_ancestor

class TestBinaryTreeFunctions(unittest.TestCase):

    def test_max_depth(self):
        print("\n🔍 Testing max_depth - Balanced Tree")
        # Tree:
        #      3
        #     / \
        #    9  20
        #       / \
        #      15  7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = 3
        result = max_depth(root)
        print(f"Expected max depth: {expected}, Got: {result}")
        self.assertEqual(result, expected)

        print("\n🔍 Testing max_depth - Left-Skewed Tree")
        # Tree:
        #     1
        #    /
        #   2
        #  /
        # 3
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.left.left = TreeNode(3)

        expected = 3
        result = max_depth(root2)
        print(f"Expected max depth: {expected}, Got: {result}")
        self.assertEqual(result, expected)

        print("\n🔍 Testing max_depth - Single Node Tree")
        root3 = TreeNode(42)
        expected = 1
        result = max_depth(root3)
        print(f"Expected max depth: {expected}, Got: {result}")
        self.assertEqual(result, expected)

        print("\n🔍 Testing max_depth - Empty Tree")
        expected = 0
        result = max_depth(None)
        print(f"Expected max depth: {expected}, Got: {result}")
        self.assertEqual(result, expected)

    def test_lowest_common_ancestor(self):
        print("\n🔍 Testing lowest_common_ancestor - Standard Case")
        # Tree:
        #        6
        #       / \
        #      2   8
        #     / \ / \
        #    0  4 7  9
        #      / \
        #     3   5
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        p = root.left       # 2
        q = root.right      # 8
        expected = 6
        result = lowest_common_ancestor(root, p, q)
        print(f"Expected LCA: {expected}, Got: {result.val}")
        self.assertEqual(result.val, expected)

        print("\n🔍 Testing lowest_common_ancestor - Deep Nodes")
        p = root.left.right.left   # 3
        q = root.left.right.right  # 5
        expected = 4
        result = lowest_common_ancestor(root, p, q)
        print(f"Expected LCA: {expected}, Got: {result.val}")
        self.assertEqual(result.val, expected)

        print("\n🔍 Testing lowest_common_ancestor - One Node is Ancestor")
        p = root.left     # 2
        q = root.left.right  # 4
        expected = 2
        result = lowest_common_ancestor(root, p, q)
        print(f"Expected LCA: {expected}, Got: {result.val}")
        self.assertEqual(result.val, expected)

if __name__ == '__main__':
    print("🧪 Running Binary Tree Lab Tests...")
    unittest.main()