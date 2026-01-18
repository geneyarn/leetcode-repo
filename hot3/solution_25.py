# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        pre, cur, nxt = None, head, None

        while cur != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        p = head
        for i in range(k):
            if not p:
                return head
            p = p.next

        sub = self.reverseKGroup(p, k)
        newHead = self.reverse(head, p)
        head.next = sub
        return newHead


result = Solution().reverse(ListNode(1, ListNode(2, ListNode(3))), None)
print(result)
