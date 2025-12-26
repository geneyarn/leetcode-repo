from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = len(nums)

        preSum = [0] * (m + 1)
        val2CountMp = {}
        val2CountMp[0] = 1
        res = 0
        for i in range(m):
            preSum[i + 1] = preSum[i] + nums[i]

            reminder = preSum[i + 1] % k
            if reminder < 0:
                reminder += k

            if reminder in val2CountMp:
                count = val2CountMp[reminder]
                res += count
                val2CountMp[reminder] = count + 1
            else:
                val2CountMp[reminder] = 1
        return res


result = Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
print(result)
