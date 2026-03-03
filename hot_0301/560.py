from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = len(nums)

        preSum = [0] * (m + 1)
        for i in range(m):
            preSum[i + 1] = preSum[i] + nums[i]

        mp = {}
        ans = 0
        for i in range(len(preSum)):
            n = preSum[i]

            if n - k in mp:
                ans += mp[n - k]
            mp[preSum[i]] = mp.get(preSum[i], 0) + 1

        return ans


result = Solution().subarraySum([1, 1, 1], 2)
print(result)
