from typing import List, Optional
from helper import TreeNode, ListNode, parse_pre_order_tree


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.m1(head)

    def m1(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        pre = slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                pre = slow
                slow = slow.next
        # if slow.next == fast:
        #     return TreeNode(slow.val, None, None)
        pre.next = None
        return TreeNode(slow.val, self.m1(head), self.m1(slow.next))

