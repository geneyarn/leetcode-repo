from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = len(nums)
        res = [0] * m
        cur = m - 1
        i, j = 0, m - 1

        while i <= j:
            if abs(nums[i]) <= abs(nums[j]):
                res[cur] = nums[j] ** 2
                j -= 1
            else:
                res[cur] = nums[i] ** 2
                i += 1
            cur -= 1
        return res


result = Solution().sortedSquares([-4, -1, 0, 3, 10])
print(result)
