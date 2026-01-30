from typing import List


class Solution:

    def twoSum(self, nums: List[int], i: int, j: int, target: int) -> List[int]:

        l, r = i, j
        ans = []
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                ans.append([nums[l], nums[r]])
                n1, n2 = nums[l], nums[r]
                while l + 1 < len(nums) and n1 == nums[l + 1]:
                    l += 1
                while r - 1 >= 0 and n2 == nums[r - 1]:
                    r -= 1
            if s < target:
                l += 1
            else:
                r -= 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            tmp = self.twoSum(nums, i + 1, len(nums) - 1, 0 - nums[i])
            for t in tmp:
                ans.append([nums[i], t[0], t[1]])
        return ans


result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(result)
