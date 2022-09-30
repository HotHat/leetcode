from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.method2(root)

    def exist(self, root, level, mid):
        bit = 1 << level - 1
        node = root
        while bit > 0:
            if bit & mid:
                node = node.right
            else:
                node = node.left
            if node is None:
                return False
            bit >>= 1

        return True

    def method1(self, root):
        if root is None:
            return 0
        level = -1
        node = root
        while node:
            level += 1
            node = node.left

        mn = 2 ** level
        mx = 2 ** (level + 1) - 1

        while mn < mx:
            mid = int((mx - mn + 1) / 2) + mn

            if self.exist(root, level, mid):
                mn = mid
            else:
                mx = mid - 1

        return mn


    def method2(self, root):
        if root is None:
            return 0

        left_level = 0
        right_level = 0

        node = root
        while node:
            left_level += 1
            node = node.left

        node = root
        while node:
            right_level += 1
            node = node.right

        if left_level == right_level:
            return 2 ** left_level - 1
        else:
            return self.method2(root.left) + self.method2(root.right) + 1

