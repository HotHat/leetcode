from typing import List, Optional
from helper import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.m2(root)

    def inorder(self, root, lst):
        if root is None:
            return
        self.inorder(root.left, lst)
        lst.append(root)
        self.inorder(root.right, lst)

    def swap(self, x, y):
        tmp = x.val
        x.val = y.val
        y.val = tmp

    def m1(self, root):
        lst = []
        self.inorder(root, lst)
        x = None
        y = None

        for i in range(1, len(lst)):
            # smaller than preview
            if lst[i].val < lst[i - 1].val:
                if x is None:
                    x = lst[i - 1]
                y = lst[i]

        self.swap(x, y)

    def m2(self, root):
        stack = []
        x = y = None
        pred = None
        s = root
        while stack or s is not None:
            while s is not None:
                stack.append(s)
                s = s.left
            s = stack.pop()
            # this place
            if pred and pred.val > s.val:
                if x is None:
                    x = pred
                y = s

            pred = s
            print(s.val)

            s = s.right

        self.swap(x, y)

