# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, head: ListNode, tail: ListNode):
        cur = d = ListNode(-1)
        p1, p2 = head, tail

        while p1 and p2:
            if p1.val <= p2.val:
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
        return d.next

    def mergeSort(self, head: ListNode, tail: ListNode):
        if not head:
            return
        if head.next == tail:
            head.next = None
            return head
        fast, slow = head, head
        while fast != tail:
            fast = fast.next
            if fast != tail:
                fast = fast.next
            slow = slow.next

        p1 = self.mergeSort(head, slow)
        p2 = self.mergeSort(slow, tail)
        return self.merge(p1, p2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head, None)
