from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pre = None
        idx = root
        # find node
        while idx:
            if idx.val == key:
                # find it
                break
            elif idx.val < key:
                pre = idx
                idx = idx.right
            else:
                pre = idx
                idx = idx.left
        # not find
        if idx is None:
            return root
        # delete root
        # if pre is None:
        #     del root
        #     return None
        sn = None

        # leaf
        if idx.left is None and idx.right is None:
            if pre is None:
                root = None
            elif pre.left == idx:
                pre.left = idx.right
            else:
                pre.right = idx.right
            del idx
            return root
        # not left
        elif idx.left is None:
            sn = idx.right
        # not right
        elif idx.right is None:
            sn = idx.left

        # single child
        if sn:
            if pre is None:
                root = sn
                return root
            elif pre.left == idx:
                pre.left = sn
            else:
                pre.right = sn
            return root

        p = idx
        cur = idx
        nxt = idx.right
        while nxt.left:
            p = nxt
            nxt = nxt.left
        cur.val = nxt.val
        if p.left == nxt:
            p.left = nxt.right
        else:
            p.right = nxt.right
        del nxt
        return root
