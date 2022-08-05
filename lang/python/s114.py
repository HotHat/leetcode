from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.m1(root)

    def pre(self, root):
        lf = root.left
        while lf.right:
            lf = lf.right
        return lf

    def m1(self, root):
        if root is None:
            return
        s = root
        while s:
            if s.left is None:
                s = s.right
            else:
                p = self.pre(s)
                p.right = s.right
                s.right = s.left
                s.left = None
                s = s.right
