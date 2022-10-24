from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        stack = [root]
        stackPath = [str(root.val)]
        res = []

        while stack:
            node = stack.pop()
            path = stackPath.pop()

            if node.left is None and node.right is None:
                res.append(path)

            if node.right:
                stack.append(node.right)
                stackPath.append(path + "->" + str(node.right.val))

            if node.left:
                stack.append(node.left)
                stackPath.append(path + "->" + str(node.left.val))

        return res
