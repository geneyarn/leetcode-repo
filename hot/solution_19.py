# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findNthFromEnd(self, head: Optional[ListNode], n: int) -> ListNode:
        p1 = head
        for i in range(n):
            p1 = p1.next

        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        x = self.findNthFromEnd(dummy, n + 1)
        x.next = x.next.next

        return dummy.next
