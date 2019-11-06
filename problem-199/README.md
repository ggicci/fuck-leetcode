# 199. Binary Tree Right Side View

Problem: https://leetcode.com/problems/binary-tree-right-side-view/

## Python Solution

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # Record node with level as a pair (node, level).
        queue = [(root, 0)]
        
        res = []
        last_level = -1
        while queue:
            cur, level = queue.pop(0)
            if level > last_level:
                res.append(cur.val)
                last_level = level
            if cur.right:
                queue.append((cur.right, level+1))
            if cur.left:
                queue.append((cur.left, level+1))

        return res
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNDE5MTM3ODA3XX0=
-->