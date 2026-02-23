# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = d = ListNode(-1, head)
        for i in range(n + 1):
            fast = fast.next

        slow = d
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return d.next
