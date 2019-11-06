# 101. Symmetric Tree

Problem: https://leetcode.com/problems/symmetric-tree/

## Python Solution

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.is_symmetric(root.left, root.right)
    
    def is_symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left != right:
            return False
        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0ODI3MDA2NzhdfQ==
-->