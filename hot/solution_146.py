class Node:

    def __init__(self, k: int, v: int):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class DoubleList:

    def __init__(self):
        self._size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addLast(self, n: Node):
        last = self.tail.prev

        last.next = n
        n.prev = last
        n.next = self.tail
        self.tail.prev = n
        self._size += 1

    def remove(self, n: Node):
        prev = n.prev
        nxt = n.next

        prev.next = nxt
        nxt.prev = prev

        self._size -= 1

        return n

    def removeFirst(self):
        if self.head.next == self.tail:
            return None

        self._size -= 1
        d = self.head.next
        self.head.next = d.next
        d.prev = self.head
        d.next.prev = self.head

        return d


class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self._list = DoubleList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.mp:
            self.makeRencent(self.mp[key])
            return self.mp[key].v
        else:
            return -1

    def makeRencent(self, n: Node):
        self._list.remove(n)
        self._list.addLast(n)

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            d = self.mp[key]
            self._list.remove(d)
            n = Node(key, value)
            self._list.addLast(n)
            self.mp[key] = n
            return

        if self.capacity == self._list._size:
            d = self._list.removeFirst()
            self.mp.pop(d.k)

            n = Node(key, value)
            self._list.addLast(n)
            self.mp[key] = n
        else:
            n = Node(key, value)
            self._list.addLast(n)
            self.mp[key] = n


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","get","get","put","get","put","put","put","put","get","put"]
# [[1],[6],[8],[12,1],[2],[15,11],[5,2],[1,15],[4,2],[4],[15,15]]

l = LRUCache(1)
print(l.get(6))
print(l.get(8))
l.put(12, 1)
print(l.get(2))
l.put(15, 11)
l.put(5, 2)
l.put(1, 15)
l.put(4, 2)
print(l.get(4))
l.put(15, 15)
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# lRUCache = LRUCache(2);
# lRUCache.put(1, 1);
# lRUCache.put(2, 2);
# print(lRUCache.get(1))
# lRUCache.put(3, 3);
# print(lRUCache.get(2))
# lRUCache.put(4, 4);
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
