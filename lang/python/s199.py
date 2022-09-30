from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.m1(root, result)
        return result

    def m1(self, root, result):
        if root is None:
            return
        s = [root]
        level_num = 1
        level_node_num = 0
        current = 0
        pre_none = None

        while s:
            n = s.pop(0)
            current += 1

            if n.left:
                s.append(n.left)
                level_node_num += 1
            if n.right:
                s.append(n.right)
                level_node_num += 1

            # level end
            if current == level_num:
                n.next = None
                current = 0
                if pre_none:
                    pre_none.next = n
                pre_none = None
                level_num = level_node_num
                level_node_num = 0
                result.append(n.val)
            else:
                if pre_none:
                    pre_none.next = n
                # else:
                pre_none = n

        return


