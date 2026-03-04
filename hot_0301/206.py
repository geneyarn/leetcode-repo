# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sub = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return sub


result = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(result)
