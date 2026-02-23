from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        result = 0

        for n in s:
            if n - 1 in s:
                continue

            tmp = n
            r = 0
            while tmp in s:
                tmp = tmp + 1
                r += 1
                result = max(r, result)

        return result


# result = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
result = Solution().longestConsecutive([0])
print(result)
