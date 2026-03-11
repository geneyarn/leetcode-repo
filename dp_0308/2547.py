from cmath import inf
from functools import cache
from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        m = len(nums)

        @cache
        def dp(i: int) -> int:
            if i == m:
                return 0

            ans = inf
            mp = {}
            uniq = 0
            for j in range(i, m):
                c = mp.get(nums[j], 0)
                if c == 0:
                    uniq += 1
                elif c == 1:
                    uniq -= 1
                mp[nums[j]] = c + 1

                ans = min(dp(j + 1) + k + (j - i + 1) - uniq, ans)
            return ans

        res = dp(0)
        dp.cache_clear()
        return res


# result = Solution().minCost([1, 2, 1, 2, 1, 3, 3], 2)
result = Solution().minCost([1, 2, 1, 2, 1], 2)
print(result)
