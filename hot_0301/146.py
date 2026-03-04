class Node:
    def __init__(self, key: int, val: int, prev: Node = None, next: Node = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class DoubleList:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, n: Node):
        last = self.tail.prev
        last.next = n
        n.next = self.tail

        self.tail.prev = n
        n.prev = last

        self.size += 1

    def remove(self, n: Node):
        prev = n.prev
        nxt = n.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def makeLatest(self, n: Node):
        self.remove(n)
        self.add(n)

    def getEarist(self) -> Node:
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.list = DoubleList()

    def get(self, key: int) -> int:
        if key in self.mp:
            n = self.mp[key]
            self.list.makeLatest(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            old = self.mp[key]
            self.list.remove(old)

            new = Node(key, value)
            self.list.add(new)
            self.mp[key] = new
        else:
            if self.list.size == self.capacity:
                n = self.list.getEarist()
                self.mp.pop(n.key)
                self.list.remove(n)

            n = Node(key, value)
            self.list.add(n)
            self.mp[key] = n


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
