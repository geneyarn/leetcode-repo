from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = len(nums)

        curSum = 0
        res = m + 1

        left, right = 0, 0

        while right < m:
            val = nums[right]
            curSum += val
            right += 1

            while curSum >= target:
                res = min(res, right - left)

                d = nums[left]
                curSum -= d
                left += 1

        return res if res < m + 1 else 0


# result = Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
result = Solution().minSubArrayLen(4, [1, 4, 4])
print(result)
