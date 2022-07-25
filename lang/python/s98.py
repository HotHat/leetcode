from typing import List, Optional
from helper import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        t = True
        if root.left is not None:
            t = True if root.val > root.left.val else False
            t = t and self.isValidBST(root.left)

        if root.right is not None:
            t = True if root.val < root.right.val else False
            t = t and self.isValidBST(root.right)

        return t


