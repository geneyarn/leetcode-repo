from typing import List


class MonoticQueue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stk = []
        self.mxStk = []

    def push(self, val: int):
        if len(self.stk) >= self.capacity:
            l = self.stk.pop(0)
            if l == self.mxStk[0]:
                self.mxStk.pop(0)

        self.stk.append(val)
        while self.mxStk and self.mxStk[-1] < val:
            self.mxStk.pop()
        self.mxStk.append(val)

    def max(self) -> int:
        return self.mxStk[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MonoticQueue(k)
        res = []
        for i in range(len(nums)):
            if i < k - 1:
                q.push(nums[i])
            else:
                q.push(nums[i])
                res.append(q.max())
        return res


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
