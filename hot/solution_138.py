# """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# """


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(head.val)
        cur = dummy

        mp = {head: dummy}
        p = head

        while p:
            if p.next:
                if p.next not in mp:
                    mp[p.next] = Node(p.next.val)
                cur.next = mp[p.next]

            if p.random:
                if p.random not in mp:
                    mp[p.random] = Node(p.random.val)
                cur.random = mp[p.random]
            cur = cur.next
            p = p.next
        return dummy


n7 = Node(7)
n13 = Node(13)
n11 = Node(11)
n10 = Node(10)
n1 = Node(1)

n7.next = n13
n13.random = n7
n13.next = n11

n11.next = n10
n11.random = n1

n10.next = n1
n10.random = n11

n1.random = n7

result = Solution().copyRandomList(n7)
print(result)
