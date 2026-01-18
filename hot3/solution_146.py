class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoubleList:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, n: Node):
        prev = self.tail.prev

        prev.next = n
        n.next = self.tail

        self.tail.prev = n
        n.prev = prev
        self.size += 1

    def remove(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev
        self.size -= 1

    def makeLastest(self, n: Node):
        self.remove(n)
        self.add(n)

    def getEarilest(self) -> Node:
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.list = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        n = self.mp[key]
        self.list.makeLastest(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            old = self.mp[key]
            self.list.remove(old)
            new = Node(key, value)
            self.mp[key] = new
            self.list.add(new)
        else:
            new = Node(key, value)
            self.mp[key] = new
            self.list.add(new)

            if self.list.size > self.capacity:
                n = self.list.getEarilest()
                self.list.remove(n)
                self.mp.pop(n.key)


lRUCache = LRUCache(2);
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
