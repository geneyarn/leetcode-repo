from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []
        self.curSum = 0

    def backTrack(self, nums: List[int], target: int, start: int):
        if self.curSum == target:
            self.ans.append(self.track.copy())
            return
        if self.curSum > target:
            return

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.curSum += nums[i]
            self.backTrack(nums, target, i)
            self.curSum -= nums[i]
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backTrack(candidates, target, 0)
        return self.ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
