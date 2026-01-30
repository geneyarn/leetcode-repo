# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.successor = None

    def reverseN(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            self.successor = head.next
            return head

        sub = self.reverseN(head.next, k - 1)
        head.next.next = head
        head.next = self.successor
        return sub

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left > 1:
            head.next = self.reverseBetween(head.next, left - 1, right - 1)
            return head
        else:
            return self.reverseN(head, right)


# head = [1,2,3,4,5], left = 2, right = 4
result = Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
