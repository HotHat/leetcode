from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_sum = 0
        if root.left and (root.left.left is None) and (root.left.right is None):
            left_sum = root.left.val

        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
