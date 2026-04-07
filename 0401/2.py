# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = cur = ListNode(-1)

        p1, p2 = l1, l2

        tmp = 0
        while p1 or p2:
            if p1:
                tmp += p1.val
                p1 = p1.next
            if p2:
                tmp += p2.val
                p2 = p2.next

            cur.next = ListNode(tmp % 10)
            cur = cur.next
            tmp = tmp // 10
        if tmp > 0:
            cur.next = ListNode(tmp)
        return p.next
