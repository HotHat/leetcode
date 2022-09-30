from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p, q) -> 'TreeNode':
        result = {}
        self.helper(root, [root], p, q, result)
        # print([i.val for i in pa])
        # print([i.val for i in qa])
        # print(result['t'].val)
        return result['t']



    def helper(self, root, parent, p, q, result):
        if root is None:
            return

        if p == root:
            result['pa'] = parent.copy()

        if q == root:
            result['qa'] = parent.copy()

        if 'pa' in result and 'qa' in result:
            pa = result['pa']
            qa = result['qa']
            while pa and qa:
                t1 = pa.pop(0)
                t2 = qa.pop(0)
                if t1 == t2:
                    result['t'] = t1

        self.helper(root.left, parent+[root.left], p, q, result)
        self.helper(root.right, parent+[root.right], p, q, result)

    def method2(self, root, p, q):
        if p.val <= root.val <= q.val:
            return root
        if q.val <= root.val <= p.val:
            return root

        if q.val <= root.val and p.val <= root.val:
            return self.method2(root.left, p, q)

        if q.val >= root.val and p.val >= root.val:
            return self.method2(root.right, p, q)
