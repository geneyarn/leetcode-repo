from math import inf
from typing import List


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        m = len(nums)

        def dp(i: int, z: int) -> int:
            if i < 0:
                return 0

            if z == i + 1:
                return nums[i]

            ans = inf
            tmp = 0
            for l in range(i, -1, -1):
                tmp = tmp ^ nums[l]
                sub = dp(l - 1, z - 1)
                ans = max(tmp, sub)
            print(f'{i}---{ans}')
            return ans

        return dp(m - 1, k)


# result = Solution().minXor([2, 3, 3, 2], 3)
# result = Solution().minXor([1, 1, 2, 3, 1], 2)
result = Solution().minXor([1, 2, 3], 2)
print(result)
#


# print(2 ^ 1)
