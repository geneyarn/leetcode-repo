from typing import List


class Solution:

    def __init__(self):
        self.track = []
        self.ans = []

    def backTrack(self, nums: List[int], target: int, idx: int):
        if target < 0:
            return
        if target == 0:
            self.ans.append(self.track.copy())
            return

        for i in range(idx, len(nums)):
            self.track.append(nums[i])
            self.backTrack(nums, target - nums[i], i)
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backTrack(candidates, target, 0)

        return self.ans
