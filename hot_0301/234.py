# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.left = None
        self.ans = True

    def valid(self, head: ListNode):
        if not head:
            return

        self.valid(head.next)

        if head.val != self.left.val:
            self.ans = False

        self.left = self.left.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.valid(head)
        return self.ans
