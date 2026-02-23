from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, v in enumerate(nums):
            if target - v in mp:
                return [i, mp[target - v]]
            mp[v] = i

        return [-1, -1]
