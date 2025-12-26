# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        for i in range(n):
            p = p.next

        s = head
        while p:
            s = s.next
            p = p.next

        return s

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(-1, head)
        x = self.findNthFromEnd(d, n + 1)
        x.next = x.next.next

        return d.next
