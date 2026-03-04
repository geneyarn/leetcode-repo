# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)

        q = []
        for i in range(len(lists)):
            n = lists[i]
            if not n:
                continue
            heapq.heappush(q, (lists[i].val, i, lists[i]))

        while q:
            val, i, n = heapq.heappop(q)
            cur.next = n
            if n.next:
                heapq.heappush(q, (n.next.val, i, n.next))

            cur = cur.next

        return dummy.next


result = Solution().mergeKLists([
    ListNode(1, ListNode(3)),
    ListNode(2, ListNode(4))
])
print(result)
