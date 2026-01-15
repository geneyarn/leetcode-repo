from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        ans = 0
        for n in s:
            if n - 1 in s:
                continue
            count = 1
            tmp = n
            while tmp + 1 in s:
                count += 1
                tmp += 1

            ans = max(ans, count)
        return ans


result = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(result)
