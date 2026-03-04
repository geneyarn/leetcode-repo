# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findNFromEnd(self, head: ListNode, n: int):
        p = head
        while n > 0:
            p = p.next
            n -= 1

        slow = head
        while p:
            slow = slow.next
            p = p.next

        return slow

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(-1, head)

        n = self.findNFromEnd(newHead, n + 1)
        n.next = n.next.next

        return newHead.next


result = Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print(result)
