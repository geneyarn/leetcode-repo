# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)
        remainder = 0

        p1, p2 = l1, l2

        while p1 or p2:
            s = remainder
            if p1:
                s += p1.val
                p1 = p1.next

            if p2:
                s += p2.val
                p2 = p2.next

            cur.next = ListNode(s % 10)
            cur = cur.next

            remainder = s // 10

        if remainder > 0:
            cur.next = ListNode(remainder)

        return dummy.next
