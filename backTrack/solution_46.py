from typing import List


class Solution:

    def __init__(self):
        self.used = None
        self.ans = []

    def backTrack(self, nums: List[int], track: List[int]):
        if len(track) == len(nums):
            self.ans.append(track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            self.used[i] = True
            track.append(nums[i])
            self.backTrack(nums, track)
            track.pop()
            self.used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)

        self.backTrack(nums, [])
        return self.ans
