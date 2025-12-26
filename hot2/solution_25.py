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
        p = head
        for i in range(k):
            if not p:
                return head
            p = p.next

        r = self.reverse(head, p)
        sub = self.reverseKGroup(p, k)
        head.next = sub

        return r


result = Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print(result)
