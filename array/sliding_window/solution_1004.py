from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m = len(nums)
        oneCount = 0
        res = 0
        left, right = 0, 0

        while right < m:
            if nums[right] == 1:
                oneCount += 1
            right += 1

            while left < right and right - left - oneCount > k:
                if nums[left] == 1:
                    oneCount -= 1
                left += 1

            res = max(res, right - left)

        return res


result = Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(result)
