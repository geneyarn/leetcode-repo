# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)
        if not lists:
            return None

        q = []
        for i, v in enumerate(lists):
            if v:
                heapq.heappush(q, (v.val, i, v))

        while q:
            val, i, v = heapq.heappop(q)
            cur.next = v
            cur = cur.next
            if v.next:
                heapq.heappush(q, (v.next.val, i, v.next))

        return dummy.next


# [[1,4,5],[1,3,4],[2,6]]

result = Solution().mergeKLists([
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
])
print(result)
