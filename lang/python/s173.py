from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.index = root
        self.stack = []
        pass

    def next(self) -> int:
        while self.stack or self.index:
            while self.index:
                self.stack.append(self.index)
                self.index = self.index.left
            r = self.stack.pop()
            self.index = r.right
            return r.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.index is not None
