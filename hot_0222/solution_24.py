# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nxt = self.swapPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = nxt

        return newHead
