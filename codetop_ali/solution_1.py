from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)
        mp = {}
        for i, v in enumerate(nums):
            if target - v in mp:
                return [i, mp[target - v]]
            mp[v] = i
        return []


result = Solution().twoSum([2, 7, 11, 15], 9)
print(result)
