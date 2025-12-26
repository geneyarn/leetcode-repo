from typing import List


class Solution:

    def splitArrayWithMaxSum(self, nums: List[int], maxSum: int) -> int:
        res = 0
        i = 0
        while i < len(nums):
            cap = maxSum
            while i < len(nums):
                if nums[i] > cap:
                    break
                else:
                    cap -= nums[i]
                    i += 1
            res += 1
        return res

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums) + 1

        while left < right:
            mid = left + (right - left) // 2
            tm = self.splitArrayWithMaxSum(nums, mid)

            if tm < k:
                right = mid
            elif tm == k:
                right = mid
            else:
                left = mid + 1
        return left


# result = Solution().splitArray([7, 2, 5, 10, 8], 2)
result = Solution().splitArray([1, 4, 4], 3)
print(result)
