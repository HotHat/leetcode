from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    L1 = 0
    L2 = 0

    def rob(self, root: Optional[TreeNode]) -> int:
        self.L1 = self.L2 = 0
        def helper(root, level):
            if root is None:
                return
            if level % 2:
                self.L1 += root.val
            else:
                self.L2 += root.val

            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 1)
        return self.L1 if self.L1 > self.L2 else self.L2
