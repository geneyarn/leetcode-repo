# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next

        m = len(arr)
        i, j = 0, m - 1

        cur = dummy = ListNode(-1)
        while i < j:
            first = arr[i]
            second = arr[j]
            first.next = second
            second.next = None

            cur.next = first
            cur = second
            i += 1
            j -= 1

        if i == j:
            cur.next = arr[i]
            arr[i].next = None

        return dummy.next
