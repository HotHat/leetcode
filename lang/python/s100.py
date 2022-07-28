from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.m2(p, q)

    def helper(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val == n2.val and self.helper(n1.left, n2.left) and self.helper(n1.right, n2.right)

    def m1(self, p, q):
        lst = [p, q]
        while lst:
            l1 = lst.pop()
            l2 = lst.pop()
            if (not l1 and l2) or (l1 and not l2):
                return False

            if l1 and l2:
                if l1.val != l2.val:
                    return False
                else:
                    lst.append(l1.left)
                    lst.append(l2.left)
                    lst.append(l1.right)
                    lst.append(l2.right)
        return True
