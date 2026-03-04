# Definition for singly-linked list.
from typing import Optional


class ListNode:
    p

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sub = self.swapPairs(head.next.next)
        newHead = head.next
        head.next = sub
        newHead.next = head

        return newHead
