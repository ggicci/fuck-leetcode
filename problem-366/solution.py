# Leetcode Problem #366 - Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [(root, None)]
        s = {}
        res = []
        leaves = []
        while q:
            (cur, parent) = q.pop(0)
            outdegree = 0
            if cur.left:
                outdegree += 1
                q.append((cur.left, cur))
            if cur.right:
                outdegree += 1
                q.append((cur.right, cur))

            if outdegree == 0:
                leaves.append((cur, parent))
            else:
                s[cur] = [parent, outdegree]
        
        while s:
            res.append([x.val for (x, _) in leaves])
            to_remove = leaves
            leaves = []
            while to_remove:
                _, p = to_remove.pop()
                if not p:
                    continue
                s[p][1] -= 1
                if s[p][1] == 0:
                    leaves.append((p, s[p][0]))
                    del s[p]
        if leaves:
            res.append([x.val for (x, _) in leaves])

        return res

