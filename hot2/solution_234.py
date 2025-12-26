# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.res = True
        self.left = None

    def traverse(self, head: ListNode):
        if not head:
            return
        self.traverse(head.next)
        if self.left.val != head.val:
            self.res = False
        self.left = self.left.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.traverse(head)
        return self.res
