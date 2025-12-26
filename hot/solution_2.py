# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2

        tmp = 0
        head = ListNode()
        cur = head

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            s = v1 + v2 + tmp
            cur.next = ListNode(s % 10)
            tmp = s // 10

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            cur = cur.next

        if tmp > 0:
            cur.next = ListNode(tmp)

        return head.next


result = Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
print(result)
