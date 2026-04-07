# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        prev, cur, nxt = None, head, None

        while cur != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast, slow = head, head
        count = k
        while count:
            fast = fast.next
            count -= 1
        if count > 0:
            return head

        new = self.reverse(head, fast)
        sub = self.reverseKGroup(fast, k)

        head.next = sub
        return new
