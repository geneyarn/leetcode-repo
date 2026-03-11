from functools import cache
from typing import List


class Solution:

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                ans = max(dp[i][j], ans)
        return ans

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0

        @cache
        def dfs(i: int, j: int) -> int:
            nonlocal ans
            # 边界条件：如果越界，公共长度为 0
            if i < 0 or j < 0:
                return 0

            # 为了确保遍历所有的 (i, j) 组合，我们需要触发其他分支的计算
            dfs(i - 1, j)
            dfs(i, j - 1)
            res = 0
            if nums1[i] == nums2[j]:
                res = dfs(i - 1, j - 1) + 1
                ans = max(ans, res)
            return res

        dfs(m - 1, n - 1)
        dfs.cache_clear()
        return ans


result = Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
print(result)
