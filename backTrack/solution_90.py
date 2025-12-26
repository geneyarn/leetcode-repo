from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], idx: int, track: List[int]):
        self.ans.append(track.copy())

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            track.append(nums[i])
            self.backTrack(nums, idx + 1, track)
            track.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backTrack(nums, 0, [])
        return self.ans
