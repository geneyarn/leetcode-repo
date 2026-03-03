from typing import List


class MaxQueue:
    def __init__(self):
        self.queue = []
        self.stk = []

    def push(self, val: int):
        self.queue.append(val)
        while self.stk and self.stk[-1] < val:
            self.stk.pop()

        self.stk.append(val)

    def pop(self):
        first = self.queue.pop(0)
        if first == self.stk[0]:
            self.stk.pop(0)

    def max(self) -> int:
        return self.stk[0]


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        q = MaxQueue()
        arr = []
        for i in range(m):
            if i < k - 1:
                q.push(nums[i])
            else:
                q.push(nums[i])
                arr.append(q.max())
                q.pop()
        return arr


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
