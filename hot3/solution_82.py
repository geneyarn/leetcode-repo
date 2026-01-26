# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = dummy = ListNode(101)
        p = head
        mp = {}
        while p:
            mp[p.val] = mp.get(p.val, 0) + 1
            p = p.next

        p = head
        while p:
            if mp[p.val] == 1:
                cur.next = ListNode(p.val)
                cur = cur.next
            p = p.next
        return dummy.next


result = Solution().deleteDuplicates(ListNode(1,
                                              ListNode(2,
                                                       ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))

print(result)
