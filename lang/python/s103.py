from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.m1(root)

    def m1(self, root):
        if root is None:
            return []

        lst = [root]
        r = []
        idx = 1
        while lst:
            t = []
            while lst:
                t.append(lst.pop(0))
            if idx == 1:
                r.append([i.val for i in t])
            else:
                p = [i.val for i in t]
                p.reverse()
                r.append(p)
            idx *= -1
            for i in t:
                if i.left:
                    lst.append(i.left)
                if i.right:
                    lst.append(i.right)
        return r

