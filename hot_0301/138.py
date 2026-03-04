class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = dummy = Node(-1)
        mp = {}
        p = head
        while p:
            if p in mp:
                n = mp[p]
            else:
                n = Node(p.val)
                mp[p] = n
            cur.next = n

            if p.random:
                if p.random in mp:
                    nn = mp[p.random]
                else:
                    nn = Node(p.random.val)
                    mp[p.random] = nn
                n.random = nn
            cur = cur.next
            p = p.next

        return dummy.next
