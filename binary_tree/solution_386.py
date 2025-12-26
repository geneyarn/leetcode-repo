from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def traverse(self, number: int, limit: int):
        if number > limit:
            return

        self.ans.append(number)
        for i in range(number * 10, number * 10 + 10):
            self.traverse(i, limit)

    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, 10):
            self.traverse(i, n)
        return self.ans
