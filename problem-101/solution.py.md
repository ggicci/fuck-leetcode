class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.is_symmetric(root.left, root.right)
    
    def is_symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left != right:
            return False
        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjI4Mzg0NjQ0LDU3ODk3ODI2Ml19
-->