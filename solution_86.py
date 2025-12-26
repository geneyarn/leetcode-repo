from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = d1 = ListNode(-1)
        p2 = d2 = ListNode(-1)

        cur = head

        while cur:
            nxt = cur.next
            cur.next = None
            if cur.val < x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            cur = nxt
        p1.next = d2.next

        return d1.next


# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
# [1,4,3,2,5,2]
result = Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)
print(result)
