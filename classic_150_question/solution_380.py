from random import choice


class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.mp[val] = len(self.arr)
        self.arr.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        preIdx = self.mp[val]
        self.arr[preIdx] = self.arr[-1]
        self.mp[self.arr[-1]] = preIdx

        self.mp.pop(val)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()