from typing import List


class Solution:

    def __init__(self):
        self.track = []
        self.ans = []
        self.used = []

    def backTrack(self, nums: List[int]):
        if len(self.track) == len(nums):
            self.ans.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            self.used[i] = True
            self.track.append(nums[i])
            self.backTrack(nums)
            self.track.pop()
            self.used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        self.used = [False] * m
        self.backTrack(nums)

        return self.ans


result = Solution().permute([1, 2, 3])
print(result)
