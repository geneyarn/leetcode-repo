from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        @cache
        def dp(idx: int, count: int) -> int:
            if idx < 0:
                return -inf
            if count == 0:
                return max(dp(idx - 1, count), 0) + arr[idx]
            return max(dp(idx - 1, count - 1), dp(idx - 1, count) + arr[idx])

        ans = -inf

        for i in range(len(arr)):
            ans = max(ans, max(dp(i, 0), dp(i, 1)))

        return ans


result = Solution().maximumSum([1, -2, 0, 3])
print(result)
