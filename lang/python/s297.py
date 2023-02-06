from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        stack = [root]
        stackPath = [root]
        res = []

        while stack:
            node = stack.pop(0)
            # path = stackPath.pop()

            if node is None:
                continue

            # if node.left is None and node.right is None:
            #     res.append(path)
            # if node.left:
            stack.append(node.left)
            stackPath.append(node.left)

            # if node.right:
            stack.append(node.right)
            stackPath.append(node.right)

        # print(stackPath)
        s = map(lambda x: 'null' if x is None else str(x.val), stackPath)
        s = list(s)
        r = ','.join(s)

        return f"[%s]" % r.rstrip(',null')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        sp = ['[', ',', ']']

        def token(s):
            tk = []
            signal = False
            n = ''
            null = 0
            skip = 0
            for i, c in enumerate(s):
                if skip > 0:
                    skip -= 1
                    continue

                if c in sp:
                    continue

                # null
                if c in ['n', 'u', 'l', 'l']:
                    null += 1
                    if null == 4:
                        tk.append(None)
                        null = 0
                    continue

                if c == '-':
                    signal = True
                    continue

                for c1 in s[i:]:
                    if c1 in sp:
                        break
                    else:
                        n += c1
                        skip = len(n)

                m = int(n)
                n = ''
                if signal:
                    m = -m
                signal = False
                tk.append(m)

            return tk

        def build(s):
            root = None

            stack = []
            idx = 0
            ch_idx = 1
            # while idx < sz:
            for n in s:
                if n is not None:
                    c = TreeNode(n)
                    stack.append(c)
                    if root is None:
                        root = c
                else:
                    c = None

                if len(stack) > 0 and stack[0] != c:
                    # left
                    if ch_idx == 1:
                        stack[0].left = c
                        ch_idx = 2
                    else:
                        stack[0].right = c
                        ch_idx = 1
                        stack.pop(0)

            return root
        return build(token(data))
