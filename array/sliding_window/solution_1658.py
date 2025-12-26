from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        allSum = sum(nums)
        m = len(nums)

        target = allSum - x

        res = -1

        curSum = 0
        i, j = 0, 0

        while j < m:
            val = nums[j]
            curSum += val
            j += 1

            while i < j and curSum > target:
                curSum -= nums[i]
                i += 1

            if curSum == target:
                res = max(res, j - i)
        return -1 if res == -1 else m - res


# result = Solution().minOperations([1, 1, 4, 2, 3], 5)
result = Solution().minOperations(
    [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365)
print(result)
