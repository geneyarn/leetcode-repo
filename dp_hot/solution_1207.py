from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        m = len(nums)
        mx = max(nums)

        result = 1

        for i in range(-mx, mx + 1):
            dp = {nums[0]: 1}
            for j in range(1, m):
                if nums[j] - i in dp:
                    dp[nums[j]] = dp[nums[j] - i] + 1
                else:
                    dp[nums[j]] = 1
            result = max(result, max(dp.values()))

        return result


# result = Solution().longestArithSeqLength([3, 6, 9, 12])
result = Solution().longestArithSeqLength([9, 4, 7, 2, 10])
print(result)
