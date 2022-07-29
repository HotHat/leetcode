from typing import List, Optional
from helper import TreeNode, parse_pre_order_tree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.m1(preorder, inorder, 0, len(preorder), 0, len(inorder))

    def m1(self, preorder, inorder, ps, pe, ns, ne):
        if ns >= ne or ps >= pe:
            return None
        r = inorder.index(preorder[ps])
        left = self.m1(preorder, inorder, ps+1, pe, ns, r)
        right = self.m1(preorder, inorder, ps+1+r-ns, pe, r+1, ne)

        return TreeNode(preorder[ps], left, right)
