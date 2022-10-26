from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if not head or not slow.next:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return None

        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr


if __name__ == "__main__":
    n4 = ListNode(-4)
    n3 = ListNode(0, n4)
    n2 = ListNode(2, n3)
    n4.next = n2
    n1 = ListNode(1)

    s = Solution()
    r = s.detectCycle(n1)
    print(r.val if r else None)

