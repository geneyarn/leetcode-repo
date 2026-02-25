from typing import List


class Solution:

    def __init__(self):
        self.used = []
        self.track = []
        self.ans = []

    def traverse(self, nums: List[int]):
        if len(self.track) == len(nums):
            self.ans.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            self.track.append(nums[i])
            self.used[i] = True
            self.traverse(nums)
            self.used[i] = False
            self.track.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.traverse(nums)
        return self.ans
