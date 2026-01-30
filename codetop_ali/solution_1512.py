from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = len(nums)
        mp = {}

        ans = 0
        for i in range(m):
            mp[nums[i]] = mp.get(nums[i], 0) + 1

        for k in mp.keys():
            v = mp[k]

            ans += v * (v - 1) // 2

        return ans


result = Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(result)
