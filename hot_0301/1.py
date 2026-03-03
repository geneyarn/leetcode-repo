from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)

        mp = {}
        for i in range(m):
            if target - nums[i] in mp:
                return [i, mp[target - nums[i]]]
            mp[nums[i]] = i
        return [-1, -1]
