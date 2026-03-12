from cmath import inf
from functools import cache
from typing import List


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        m = len(nums)
        pre = [0] * (m + 1)
        for i in range(m):
            pre[i + 1] = pre[i] ^ nums[i]

        @cache
        def dp(i: int, k: int) -> int:
            if k == 1:
                return pre[m] ^ pre[i]

            res = inf
            for j in range(i + 1, m - k + 2):
                res = min(res, max(pre[j] ^ pre[i], dp(j, k - 1)))
            return res

        res = dp(0, k)
        dp.cache_clear()

        return res
