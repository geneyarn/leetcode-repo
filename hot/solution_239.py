from collections import deque
from typing import List


class MonoticQueue:

    def __init__(self):
        self.q = deque()

    def push(self, n: int):
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

    def max(self) -> int:
        return self.q[0]

    def pop(self, n):
        if n == self.q[0]:
            self.q.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = MonoticQueue()
        for i in range(len(nums)):
            if i < k - 1:
                q.push(nums[i])
            else:
                q.push(nums[i])
                res.append(q.max())
                q.pop(nums[i - k + 1])

        return res


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
