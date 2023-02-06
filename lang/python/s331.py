from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s = preorder.split(',')
        stk = []
        ntk = []
        for i in s:
            if i != '#':
                stk.append(i)
                ntk.append(0)
            else:
                if len(ntk) == 0:
                    continue
                ntk[-1] += 1
                while ntk[-1] == 2:
                    ntk.pop()
                    stk.pop()
                    if len(stk) == 0:
                        break
                    else:
                        ntk[-1] += 1
        return len(ntk) == 0
