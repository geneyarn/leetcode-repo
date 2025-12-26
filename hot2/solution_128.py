from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = True

        res = 0
        for k in mp.keys():
            if k - 1 in mp:
                continue
            tmp = k
            count = 1
            while tmp + 1 in mp:
                count += 1
                tmp += 1

            res = max(res, count)
        return res


result = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(result)
