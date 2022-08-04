from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # print_tree(root)
        return self.m2(root, targetSum)
        result = []
        self.m1(root, targetSum, [], result)
        return result

    def m1(self, root, target, path, result):
        if root is None:
            return
        p = path.copy()
        p.append(root.val)
        if root.left is None and root.right is None:
            if sum(p) == target:
                result.append(p)

        self.m1(root.left, target, p, result)
        self.m1(root.right, target, p, result)

    def m2(self, root, target):
        lst = []
        num_lst = []
        if root is None:
            return []

        result = []
        lst.append(root)
        num_lst.append([])
        while lst:
            cur = lst.pop(0)
            cur_num = num_lst.pop(0)
            cur_num.append(cur.val)

            if cur.left is None and cur.right is None:
                if sum(cur_num) == target:
                    result.append(cur_num)
            if cur.left:
                lst.append(cur.left)
                num_lst.append(cur_num[:])
            if cur.right:
                lst.append(cur.right)
                num_lst.append(cur_num[:])

        return result
