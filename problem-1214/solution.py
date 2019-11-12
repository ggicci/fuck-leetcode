# Leetcode Problem #1214 - Two Sum BSTs
# https://leetcode.com/problems/two-sum-bsts/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # Traverse tree of root1.
        if not root1:
            return False
        q = [root1]
        while q:
            cur = q.pop(0)
            if self.bst_search(root2, target - cur.val):
                return True

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return False

    def bst_search(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if target == root.val:
            return True
        if target < root.val:
            return self.bst_search(root.left, target)
        return self.bst_search(root.right, target)
