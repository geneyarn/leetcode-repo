# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = 0
        cur = dummy = ListNode(-1)

        p1, p2 = l1, l2

        while p1 or p2:
            v1 = 0 if not p1 else p1.val
            v2 = 0 if not p2 else p2.val

            r = (v1 + v2 + tmp)
            cur.next = ListNode(r % 10)
            tmp = r // 10
            cur = cur.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if tmp > 0:
            cur.next = ListNode(tmp)

        return dummy.next
