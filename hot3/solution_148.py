# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, p1: ListNode, p2: ListNode) -> ListNode:
        cur = dummy = ListNode(-1)

        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next

            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2

        return dummy.next

    def mergeSort(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return None
        if head.next == tail:
            head.next = None
            return head

        fast, slow = head, head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        p1 = self.mergeSort(head, slow)
        p2 = self.mergeSort(slow, tail)

        return self.merge(p1, p2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head, None)


result = Solution().sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
print(result)
