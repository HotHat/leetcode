from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.m1(root)

    def m1(self, root):
        if root is None:
            return []
        lst = [root]
        r = []
        while lst:
            t = []
            while lst:
                t.append(lst.pop(0))
            r.insert(0, [i.val for i in t])
            for i in t:
                if i.left:
                    lst.append(i.left)
                if i.right:
                    lst.append(i.right)

        return r

