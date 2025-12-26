from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        for k in mp.keys():
            if mp[k] == 1:
                return k
        return -1
