from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.m1(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def m1(self, inorder, postorder, ps, pe, ns, ne):
        if ns > ne or ps > pe:
            return None
        r = inorder.index(postorder[ne])
        m = ns+r-ps
        left = self.m1(inorder, postorder, ps, r, ns, m-1)
        right = self.m1(inorder, postorder, r+1, pe, m, ne-1)

        return TreeNode(inorder[r], left, right)
