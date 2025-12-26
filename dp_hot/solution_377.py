from functools import cache
from typing import List


class Solution:

    # @cache
    def backTrack(self, nums: List[int], idx: int, target: int) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        ans = 0
        for i in range(idx, len(nums)):
            target -= nums[i]
            ans += self.backTrack(nums, idx, target)
            target += nums[i]
        return ans

    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(newTarget: int):
            if newTarget < 0:
                return 0
            if newTarget == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                newTarget -= nums[i]
                ans += dfs(newTarget)
                newTarget += nums[i]
            return ans

        return dfs(target)


result = Solution().combinationSum4([1, 2, 3], 4)
print(result)
