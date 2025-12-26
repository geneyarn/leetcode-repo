from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        m = len(nums)

        tmp = 1
        left, right = 0, 0
        ans = 0
        while right < m:
            val = nums[right]
            tmp *= val
            right += 1

            while left < right and tmp >= k:
                tmp /= nums[left]
                left += 1
            if tmp < k:
                ans += right - left

        return ans


result = Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
# result = Solution().numSubarrayProductLessThanK([1, 2, 3], 0)
print(result)
