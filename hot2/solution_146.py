class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def add(self, n: Node):
        prev = self.tail.pre
        prev.next = n
        n.pre = prev

        n.next = self.tail
        self.tail.pre = n
        self.size += 1

    def remove(self, n: Node):
        pre = n.pre
        nxt = n.next

        pre.next = nxt
        nxt.pre = pre
        self.size -= 1

    def removeFisrt(self) -> Node:
        if self.head.next == self.tail:
            return None
        n = self.head.next
        self.remove(n)
        return n


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.list = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        n = self.mp.get(key)
        self.list.remove(n)
        self.list.add(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            old = self.mp[key]
            self.list.remove(old)
            new = Node(key, value)
            self.mp[key] = new
            self.list.add(new)
        else:
            if self.list.size >= self.capacity:
                n = self.list.removeFisrt()
                self.mp.pop(n.key)
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
