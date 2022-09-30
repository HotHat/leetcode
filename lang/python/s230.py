from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        s = []
        r = root
        kth = 0
        while s or r:
            while r:
                s.append(r)
                r = r.left
            p = s.pop()
            kth += 1
            if kth == k:
                return p.val
            # print(p.val)
            if p.right:
                r = p.right
