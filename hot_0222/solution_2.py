# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)
        p1, p2 = l1, l2

        tmp = 0
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            all = v1 + v2 + tmp
            cur.next = ListNode(all % 10)
            tmp = all // 10

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            cur = cur.next

        if tmp > 0:
            cur.next = ListNode(tmp)

        return dummy.next
