from typing import List


class Solution:

    def solve(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)

        diff = [0] * m
        for i in range(m):
            diff[i] = nums2[i] - nums1[i]

        dp = [0] * m
        dp[0] = diff[0]

        for i in range(1, m):
            dp[i] = max(dp[i - 1] + diff[i], diff[i])

        return max(dp) + sum(nums1)

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        return max(self.solve(nums1, nums2), self.solve(nums2, nums1))


result = Solution().maximumsSplicedArray(nums1=[60, 60, 60], nums2=[10, 90, 10])
print(result)
