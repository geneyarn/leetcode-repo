from functools import cache
from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []
        self.target = 0

    def backTrack(self, nums: List[int], idx: int, cur: int):
        if cur > self.target:
            return
        if cur == self.target:
            self.ans.append(self.track.copy())
            return

        for i in range(idx, len(nums)):
            self.track.append(nums[i])
            self.backTrack(nums, i, cur + nums[i])
            self.track.pop()

    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 1

            ans = 0
            for j in range(len(nums)):
                if nums[j] <= i:
                    ans += dp(i - nums[j])

            return ans

        return dp(target)


result = Solution().combinationSum4([1, 2, 3], 4)
print(result)
