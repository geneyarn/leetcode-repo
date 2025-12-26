# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, p1: ListNode, p2: ListNode) -> ListNode:
        l1, l2 = p1, p2
        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1

        if l2:
            cur.next = l2

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
