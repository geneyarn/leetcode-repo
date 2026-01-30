# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.left = None
        self.result = True

    def palindrome(self, head: ListNode):
        if not head:
            return
        self.palindrome(head.next)
        if self.left.val != head.val:
            self.result = False
        self.left = self.left.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.palindrome(head)

        return self.result
