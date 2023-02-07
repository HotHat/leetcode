from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        r = self.helper(root, targetSum)
        return r + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def helper(self, root, lft):
        if root is None:
            return 0

        if root.val == lft:
            return 1 + self.helper(root.left, lft-root.val) + self.helper(root.right, lft-root.val)

        return self.helper(root.left, lft-root.val) + self.helper(root.right, lft-root.val)

# 可用前缀和优化

