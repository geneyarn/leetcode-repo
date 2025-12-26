# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        cur = dummy = ListNode(-1)

        tmp = 0
        while p1 or p2:
            v1 = 0
            if p1:
                v1 = p1.val
                p1 = p1.next
            v2 = 0
            if p2:
                v2 = p2.val
                p2 = p2.next
            s = (v1 + v2 + tmp)
            tmp = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

        if tmp > 0:
            cur.next = ListNode(tmp)
        return dummy.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(l1, l2)
