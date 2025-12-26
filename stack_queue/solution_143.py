# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = []
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next

        res.pop(0)

        p = head
        while res:
            p.next = res.pop()
            if res:
                p.next.next = res.pop(0)
                p = p.next.next
                p.next = None
            else:
                p = p.next
                p.next = None
        return head


result = Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
# result = Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(result)
