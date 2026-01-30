from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = len(nums)
        preSum = [0] * (m + 1)
        for i in range(m):
            preSum[i + 1] = preSum[i] + nums[i]

        mp = {0: 1}
        ans = 0
        for i in range(1, m + 1):
            target = preSum[i] - k
            if target in mp:
                ans += mp[target]
            mp[preSum[i]] = mp.get(preSum[i], 0) + 1

        return ans


result = Solution().subarraySum([1, 1, 1], 2)
print(result)
