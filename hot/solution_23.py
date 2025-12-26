# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []
        dummy = ListNode(-1)
        cur = dummy
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            val, i, head = heapq.heappop(pq)
            cur.next = head
            if head.next:
                heapq.heappush(pq, (head.next.val, i, head.next))

            cur = cur.next
        return dummy.next
