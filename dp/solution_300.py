from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pipes = [0] * len(nums)
        cur = 0

        for n in nums:
            i, j = 0, cur

            while i < j:
                mid = (i + j) // 2
                if pipes[mid] >= n:
                    j = mid
                else:
                    i = mid + 1

            if i == cur:
                cur += 1
            pipes[i] = n
        return cur


result = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(result)
