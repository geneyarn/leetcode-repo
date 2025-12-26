from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = len(nums)
        preSum = [0] * (m + 1)
        for i in range(1, m + 1):
            preSum[i] = nums[i - 1] + preSum[i - 1]
        mp = {0: 1}
        res = 0
        for i in range(1, m + 1):
            need = preSum[i] - k
            if need in mp:
                res += mp[need]
            mp[preSum[i]] = mp.get(preSum[i], 0) + 1
        return res


result = Solution().subarraySum([1, 1, 1], 2)
print(result)
