from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur_set = set(nums)

        res = 0
        for n in nums:
            if n - 1 not in cur_set:
                count = 1
                cur = n
                while cur + 1 in cur_set:
                    count += 1
                    cur = cur + 1
                res = max(res, count)

        return res


result = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(result)
