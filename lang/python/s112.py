from typing import Optional
from lang.python.helper import TreeNode, print_tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # print_tree(root)
        return self.m1(root, targetSum, 0)

    def m1(self, root, target, num):
        if root is None:
            return False

        # leaf
        if root.left is None and root.right is None:
            return target == root.val + num
        elif root.left is None:
            return self.m1(root.right, target, num+root.val)
        elif root.right is None:
            return self.m1(root.left, target, num+root.val)

        return self.m1(root.left, target, num+root.val) or self.m1(root.right, target, num+root.val)
