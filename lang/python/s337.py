from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def __init__(self):
        self.f = {}
        self.g = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return max(self.f[root], self.g[root])

    def helper(self, root):
        if root is None:
            self.f[root] = self.g[root] = 0
            return 0
        self.helper(root.left)
        self.helper(root.right)
        f = root.val + self.g[root.left] + self.g[root.right]
        g = max(self.f[root.left], self.g[root.left]) + max(self.f[root.right], self.g[root.right])
        self.f[root] = f
        self.g[root] = g

    # def f(self, root):
    #     if root is None:
    #         return 0
    #     return root.val + self.g(root.left) + self.g(root.right)
    #
    # def g(self, root):
    #     if root is None:
    #         return 0
    #     return max(self.f(root.left), self.g(root.left)) + max(self.f(root.right), self.g(root.right))


# f(o) = g(left) + g(right) + o.val
# g(o) = max(f(left), g(left)) + max(f(right), g(right))