from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.m1(root)

    def m1(self, root):
        if root is None:
            return root

        s = [root]
        level_num = 1
        current = 0
        pre_none = None

        while s:
            n = s.pop(0)
            current += 1

            # level end
            if current == level_num:
                n.next = None
                level_num *= 2
                current = 0
                if pre_none:
                    pre_none.next = n
                pre_none = None
            else:
                if pre_none:
                    pre_none.next = n
                pre_none = n

            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        return root
