# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode(-1)

        q = []
        for i in range(len(lists)):
            l = lists[i]
            if not l:
                continue

            heapq.heappush(q, (l.val, i, l))

        while q:
            val, i, l = heapq.heappop(q)
            cur.next = l
            cur = cur.next

            if l.next:
                heapq.heappush(q, l.next)

        return dummy.next
