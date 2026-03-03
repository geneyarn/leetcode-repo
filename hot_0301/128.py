from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = len(nums)
        s = set()

        for i in range(m):
            s.add(nums[i])

        ans = 0
        for i in range(m):
            n = nums[i]
            if n - 1 in s:
                continue
            count = 0
            tmp = n
            while tmp in s:
                count += 1
                tmp += 1
            ans = max(ans, count)

        return ans
