from typing import List, Optional
from helper import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root, lst):
            if root is None:
                return
            inorder(root.left, lst)
            lst.append(root)
            inorder(root.right, lst)

        def swap(x, y):
            tmp = x.val
            x.val = y.val
            y.val = tmp

        lst = []
        inorder(root, lst)
        x = None
        y = None

        for i in range(1, len(lst)):
            # smaller than preview
            if lst[i].val < lst[i - 1].val:
                if x is None:
                    x = lst[i - 1]
                y = lst[i]

        swap(x, y)
