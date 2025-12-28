from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        m = len(nums)

        ans = 0
        for k in range(2, m):
            v = nums[k]
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > v:
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1
        return ans

result = Solution().triangleNumber([2,2,3,4])
print(result)

