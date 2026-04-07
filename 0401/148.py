# Definition for singly-linked list.
from dis import LOAD_SMALL_INT
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
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

    def sort(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return head

        if head.next == tail:
            head.next = None
            return head

        fast, slow = head, head
        while fast != tail:
            fast = fast.next
            slow = slow.next
            if fast != tail:
                fast = fast.next

        l1 = self.sort(head, slow)
        l2 = self.sort(slow, tail)

        return self.merge(l1, l2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sort(head, None)
