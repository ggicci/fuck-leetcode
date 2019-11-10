# Leetcode Problem #112 - Path Sum
# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        return self.dfs([root], sum)

    def dfs(self, path: List[TreeNode], target: int) -> bool:
        cur = path[-1]

        if not cur.left and not cur.right:
            # is leaf
            if target == cur.val:
                return True
        if cur.left:
            if self.dfs(path + [cur.left], target - cur.val):
                return True
        if cur.right:
            if self.dfs(path + [cur.right], target - cur.val):
                return True
        return False
