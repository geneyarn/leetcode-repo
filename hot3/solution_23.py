# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i, n in enumerate(lists):
            if not n:
                continue
            heapq.heappush(pq, (n.val, i, n))

        cur = dummy = ListNode(-1)

        while pq:
            val, i, node = heapq.heappop(pq)
            cur.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            cur = cur.next
        return dummy.next
