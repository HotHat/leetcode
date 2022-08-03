from typing import Optional
from lang.python.helper import TreeNode, print_tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # print_tree(root)
        return self.m1(root)

    def m1(self, root):
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.m1(root.right)
        if root.right is None:
            return 1 + self.m1(root.left)
        return 1 + min(self.m1(root.left), self.m1(root.right))
