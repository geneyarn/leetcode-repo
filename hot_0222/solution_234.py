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

    def palindrome(self, head: ListNode):
        if not head:
            return
        self.palindrome(head.next)
        if self.left.val != head.val:
            self.ans = False
        self.left = self.left.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.palindrome(head)
        return self.ans

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next

        i, j = 0, len(arr) - 1

        while i < j:
            if arr[i].val != arr[j].val:
                return False
            i += 1
            j -= 1
        return


result = Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2))))
