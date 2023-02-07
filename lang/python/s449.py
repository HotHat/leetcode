from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        ret = str(root.val)
        ret += '' if l == '' else ',' + l
        ret += '' if r == '' else ',' + r
        return ret

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == '':
            return None
        return self.builder(data.split(','))

    def builder(self, data):
        if len(data) == 0:
            return None
        val = int(data[0])
        left = []
        right = []
        for i in data:
            i = int(i)
            if i < val:
                left.append(i)
            elif i > val:
                right.append(i)
        l = self.builder(left)
        r = self.builder(right)
        return TreeNode(val, l, r)






