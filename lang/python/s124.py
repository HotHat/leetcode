from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    maxVal = -10000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maxVal = root.val
        self.maxSum(root)
        return self.maxVal

    def maxSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l = self.maxSum(root.left)
        r = self.maxSum(root.right)

        l1 = root.val
        l2 = root.val + l
        l3 = root.val + r
        l4 = root.val + l + r
        m = max(l1, l2, l3, l4)

        self.maxVal = max(self.maxVal, m)
        return max(l1, l2, l3)
