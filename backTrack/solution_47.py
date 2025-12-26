from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.used = None
        self.track = []

    def backTrack(self, nums: List[int]):
        if len(self.track) == len(nums):
            self.ans.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue

            self.used[i] = True
            self.track.append(nums[i])
            self.backTrack(nums)
            self.track.pop()
            self.used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.used = [False] * len(nums)
        self.backTrack(nums)
        return self.ans


result = Solution().permuteUnique([1, 2, 2])
print(result)
