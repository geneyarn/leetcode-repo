# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        cur = head
        pre = None
        nxt = None

        while cur != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for i in range(k):
            if not cur:
                return head
            cur = cur.next

        n = self.reverse(head, cur)
        nxt = self.reverseKGroup(cur.next, k)
        n.next = nxt
        return n
