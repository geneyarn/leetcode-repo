class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, n: Node):
        prev = self.tail.prev
        prev.next = n
        n.prev = prev

        n.next = self.tail
        self.tail.prev = n

        self.size += 1

    def remove(self, n: Node):
        prev = n.prev
        nxt = n.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def makeLastest(self, n: Node):
        self.remove(n)
        self.insert(n)

    def getEarist(self) -> Node:
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.list = DoubleList()
        self.capacity = capacity

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
            self.mp.pop(old.key)

            new = Node(key, value)
            self.list.insert(new)
            self.mp[key] = new
        else:
            new = Node(key, value)
            self.list.insert(new)
            self.mp[key] = new
            if self.list.size > self.capacity:
                old = self.list.getEarist()
                self.list.remove(old)
                self.mp.pop(old.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
