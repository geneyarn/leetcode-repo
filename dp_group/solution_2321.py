from typing import List


class Solution:

    def solve(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        dp = [0] * (m + 1)

        for i in range(m):
            diff = nums2[i] - nums1[i]
            dp[i + 1] = max(dp[i] + diff, diff, 0)

        return sum(nums1) + max(dp)

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        return max(self.solve(nums1, nums2), self.solve(nums2, nums1))


# result = Solution().solve([60, 60, 60], [10, 90, 10])
result = Solution().solve([20, 40, 20, 70, 30], [50, 20, 50, 40, 20])
print(result)
