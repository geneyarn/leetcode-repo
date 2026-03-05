from typing import List


class Solution:

    def __init__(self):
        self.used = []
        self.ans = []

    def backTrack(self, nums: List[int], track: List[int]):
        if len(track) == len(nums):
            self.ans.append(track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            track.append(nums[i])
            self.used[i] = True
            self.backTrack(nums, track)
            self.used[i] = False
            track.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        self.used = [False] * m
        self.backTrack(nums, [])
        return self.ans
