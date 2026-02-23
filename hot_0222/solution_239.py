from typing import List


class MaxQueue:
    def __init__(self):
        self.maxStk = []

    def push(self, n: int):
        while self.maxStk and self.maxStk[-1] < n:
            self.maxStk.pop()
        self.maxStk.append(n)

    def max(self) -> int:
        return self.maxStk[0]

    def pop(self, n: int):
        if n == self.maxStk[0]:
            self.maxStk.pop(0)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        stk = MaxQueue()
        ans = []
        for i in range(m):
            n = nums[i]
            if i < k - 1:
                stk.push(n)
            else:
                stk.push(n)
                ans.append(stk.max())
                stk.pop(i - k + 1)
        return ans


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
