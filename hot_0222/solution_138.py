class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}

        p = head
        cur = dummy = Node(-1)

        while p:
            if p in mp:
                cur.next = mp[p]
            else:
                mp[p] = Node(p.val)
                cur.next = mp[p]

            if p.random:
                if p.random not in mp:
                    mp[p.random] = Node(p.random.val)
                cur.next.random = mp[p.random]
            cur = cur.next
            p = p.next
        return dummy.next
