from typing import List


class Solution:

    def twoSum(self, nums: List[int], start: int, target: int) -> List[int]:
        res = []
        i, j = start, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                l, r = nums[i], nums[j]
                res.append([l, r])
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
            tmp = self.twoSum(nums, i + 1, -nums[i])
            for t in tmp:
                res.append([nums[i], t[0], t[1]])
            n = nums[i]
            while i < len(nums) and nums[i] == n:
                i += 1

        return res


result = Solution().threeSum([-1, 0, 1, 2, -1, -4])

# result = Solution().threeSum([0, 0, 0])
print(result)
