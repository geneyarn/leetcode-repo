# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        mp = {}
        cur = dummy = Node(-1)
        p = head

        while p:
            if p not in mp:
                mp[p] = Node(p.val)
            cur.next = mp[p]
            if p.random:
                if p.random not in mp:
                    mp[p.random] = Node(p.random.val)
                cur.next.random = mp[p.random]
            cur = cur.next
            p = p.next
        return dummy.next
