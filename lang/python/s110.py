from typing import List, Optional
from helper import TreeNode, print_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        m = abs(self.m1(root.left) - self.m1(root.right))
        return m <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def m1(self, root):
        if root is None:
            return 0
        return 1 + max(self.m1(root.left), self.m1(root.right))

