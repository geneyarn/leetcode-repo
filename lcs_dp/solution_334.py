from functools import cache
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m = len(nums)
        pies = [0] * m
        cur = 0

        for i in range(m):
            v = nums[i]
            l, r = 0, cur

            while l < r:
                mid = (l + r) // 2
                if pies[mid] >= v:
                    r = mid
                else:
                    l = mid + 1
            if l == cur:
                cur += 1
            pies[l] = v

        return cur >= 3

    def increasingTriplet2(self, nums: List[int]) -> bool:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            ans = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp(j) + 1)

            return ans

        mx = max([dp(i) for i in range(m)])
        return mx >= 3


result = Solution().increasingTriplet([4, 5, 2147483647, 1, 2])
# result = Solution().increasingTriplet([1, 2, 3, 4, 5])
print(result)
