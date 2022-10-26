from typing import Optional, List
from lang.python.helper import TreeNode, print_tree


class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == "__main__":
    n4 = ListNode(-4)
    n3 = ListNode(0, n4)
    n2 = ListNode(2, n3)
    n4.next = n2
    n1 = ListNode(3, n2)

    s = Solution()
    r = s.hasCycle(n1)
    print(r)

