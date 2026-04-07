# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def find(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new = ListNode(-1, head)

        p = self.find(new, n + 1)
        p.next = p.next.next

        return new.next
