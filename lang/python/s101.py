from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.m3(root)

    def m1(self, root):
        if root is None:
            return True
        l = self.lr(root.left)
        r = self.rr(root.right)
        print(l)
        print(r)
        return l == r

    def lr(self, root):
        r = ''
        if root is None:
            return '*'
        r += self.lr(root.left)
        r += self.lr(root.right)
        r += str(root.val)
        return r

    def rr(self, root):
        r = ''
        if root is None:
            return '*'
        r += self.rr(root.right)
        r += self.rr(root.left)
        r += str(root.val)
        return r
        # print(root.val, ' ', end='')

    def sym(self, ar):
        sz = len(ar)
        for i in range(sz):
            s = sz - i - 1
            if i >= s:
                break
            if (ar[i] is None or ar[s] is None) and ar[i] != ar[s]:
                return False
            if (ar[i] and ar[s]) and ar[i].val != ar[s].val:
                return False
        return True

    def m2(self, root):
        lst = [root]
        while lst:
            lt = []
            while lst:
                lt.append(lst.pop())
            t = self.sym(lt)
            if not t:
                return False
            for i in lt:
                if i:
                    lst.append(i.left)
                    lst.append(i.right)
        return True

    def m3(self, root):
        def helper(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and helper(n1.left, n2.right) and helper(n1.right, n2.left)
        if root is None:
            return True
        return helper(root.left, root.right)
