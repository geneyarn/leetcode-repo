from typing import List


class Solution:

    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        res = []
        i, j = start, len(nums) - 1

        while i < j:
            s = nums[i] + nums[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                res.append([nums[i], nums[j]])
                l, r = nums[i], nums[j]
                while i < j and nums[i] == l:
                    i += 1
                while i < j and nums[j] == r:
                    j -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            n = nums[i]

            tmp = self.twoSum(nums, i + 1, 0 - n)
            for a in tmp:
                a.append(n)
                res.append(a)

            while i < len(nums) and nums[i] == n:
                i += 1

        return res


result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(result)
