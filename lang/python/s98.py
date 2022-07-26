from typing import List, Optional
from helper import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root, mn, mx):
            if root is None:
                return True

            if mn is not None and root.val <= mn:
                return False
            if mx is not None and mx <= root.val:
                return False

            return help(root.left, mn, root.val) and help(root.right, root.val, mx)
            # t = True
            # if root.left is not None:
            #     if root.left.val < root.val:
            #         t = help(root.left, mn, root.val)
            #     else:
            #         return False
            #
            # if not t:
            #     return False
            #
            # if root.right is not None:
            #     if root.val < root.right.val:
            #         t = help(root.right, root.val, mx)
            #     else:
            #         return False
            # return t
        return help(root, None, None)


