from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, v in enumerate(nums):
            mp[v] = i

        for i, v in enumerate(nums):
            if target - v in mp and mp[target - v] != i:
                return [i, mp[target - v]]
        return [-1, -1]


result = Solution().twoSum([3, 2, 4], 6)
print(result)
