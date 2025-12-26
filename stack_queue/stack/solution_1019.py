# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next

        m = len(arr)
        stk = []
        res = [0] * len(arr)

        for i in range(m - 1, -1, -1):
            while stk and stk[-1] <= arr[i]:
                stk.pop()
            res[i] = 0 if not stk else stk[-1]
            stk.append(arr[i])

        return res
