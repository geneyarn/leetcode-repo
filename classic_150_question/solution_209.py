from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = len(nums)

        cur_sum = 0
        i = j = 0
        ans = m + 1
        while j < len(nums):
            cur_sum += nums[j]
            j += 1

            while cur_sum >= target:
                if cur_sum == target:
                    ans = min(ans, j - i)
                cur_sum -= nums[i]
                i += 1
        return ans if ans < target + 1 else -1


result = Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(result)
