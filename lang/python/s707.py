from typing import Optional, List
from lang.python.helper import TreeNode, print_tree

from lang.python.helper import TreeNode

class MyLinkedList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.root = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        r = self.root
        while r:
            if index == 0:
                break
            index -= 1
            r = r.next

        if not r:
            return -1

        return r.val

    def addAtHead(self, val: int) -> None:
        n = self.Node(val, self.root)
        self.root = n


    def addAtTail(self, val: int) -> None:
        if not self.root:
            self.root = self.Node(val)
            return

        r = self.root
        while r.next:
            r = r.next

        r.next = self.Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        # if not self.root:
        #     self.root = self.Node(val)
        #     return

        if index <= 0:
            self.addAtHead(val)
            return

        index -= 1
        r = self.root
        while r and r.next:
            if index == 0:
                break
            index -= 1
            r = r.next

        if index == 0 and self.root:
            n = self.Node(val, r.next)
            r.next = n

    def deleteAtIndex(self, index: int) -> None:
        if not self.root:
            return None
        if index == 0 and self.root:
            self.root = self.root.next
            return

        index -= 1
        r = self.root
        while r.next:
            if index <= 0:
                break
            index -= 1
            r = r.next

        if r.next:
            r.next = r.next.next


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    linkedList = MyLinkedList()
    # linkedList.addAtHead(1)
    # linkedList.addAtHead(2)
    # linkedList.addAtHead(3)
    # linkedList.addAtHead(4)
    # -------- example ------
    # linkedList.addAtTail(1)
    # linkedList.addAtTail(3)
    # s = linkedList.get(1)
    # print(s)
    # --------------
    # -------- example 1------
    # linkedList.addAtHead(1)
    # linkedList.addAtTail(3)
    # linkedList.addAtIndex(1, 2)
    # s = linkedList.get(1)
    # print(s)
    # linkedList.deleteAtIndex(1)
    # s = linkedList.get(1)
    # print(s)
    # --------------
    # ---------example 2---------
    linkedList.addAtIndex(0, 10)
    linkedList.addAtIndex(0, 20)
    linkedList.addAtIndex(1, 30)
    s = linkedList.get(0)
    print(s)
    # ---------------------------

    # linkedList.addAtTail(6)
    # linkedList.addAtTail(7)
    # linkedList.addAtTail(8)
    # linkedList.addAtIndex(1, 0)
    # s = linkedList.get(1)
    # print(s)
    # linkedList.addAtIndex(5, 6)
    # linkedList.deleteAtIndex(6) # 现在链表是1-> 3
    # linkedList.addAtIndex(2, 7)
    # linkedList.addAtIndex(3, 8)
    # s = linkedList.get(1) # 返回2
    # print(s)
    # linkedList.deleteAtIndex(0) # 现在链表是1-> 3
    # linkedList.addAtIndex(0, 4) # 链表变为1-> 2-> 3
    # s = linkedList.get(4) # 返回3
    # print(s)
    r = linkedList.root
    n = 0
    print('----------')
    while r:
        print(linkedList.get(n))
        n += 1
        r = r.next
