from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], track: List[int], idx: int):
        self.ans.append(track.copy())

        for i in range(idx, len(nums)):
            track.append(nums[i])
            self.backTrack(nums, track, i + 1)
            track.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backTrack(nums, [], 0)
        return self.ans
