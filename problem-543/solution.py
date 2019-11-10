# Leetcode Problem #543 - Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mem = {}
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_depth(root)
        return self.res

    def max_depth(self, root: TreeNode) -> tuple:
        """Find max depth of root. And build the cache simultaneously.

        Returns:
            left_max_depth: The max depth of left subtree.
            right_max_depth: The max depth of right subtree.
        """
        if not root:
            return (0, 0)

        if root in self.mem:
            # Hit cache.
            return self.mem[root]

        left = 0
        right = 0
        if root.left:
            left = max(self.max_depth(root.left)) + 1
        if root.right:
            right = max(self.max_depth(root.right)) + 1

        self.res = max(self.res, left + right)

        cache = (left, right)
        self.mem[root] = cache
        return cache
