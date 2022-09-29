from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.sum

    def helper(self, root, inter) -> int:
        if root is None:
            return 0

        # leaf
        if root.left is None and root.right is None:
            s = root.val + inter * 10
            self.sum += s

        inter = inter * 10 + root.val
        self.helper(root.left, inter)
        self.helper(root.right, inter)

