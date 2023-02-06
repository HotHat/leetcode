from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s = preorder.split(',')
        ntk = [0]
        for i in s:
            if i != '#':
                ntk.append(0)
            else:
                if len(ntk) == 0:
                    break
                ntk[-1] += 1
                while ntk[-1] == 2:
                    ntk.pop()
                    if len(ntk) == 0:
                        break
                    else:
                        ntk[-1] += 1
        return len(ntk) == 1 and ntk[0] == 1
