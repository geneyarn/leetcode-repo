from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        ans = 0
        for n in s:
            if n - 1 in s:
                continue

            cur = n
            tmp = 0
            while cur in s:
                tmp += 1
                cur += 1
            ans = max(ans, tmp)

        return ans


result = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(result)
