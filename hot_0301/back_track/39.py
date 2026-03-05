from typing import List


class Solution:

    def __init__(self):
        self.target = 0
        self.track = []
        self.ans = []

    def backTrack(self, nums: List[int], idx: int, cur: int):
        if cur > self.target:
            return
        if cur == self.target:
            self.ans.append(self.track.copy())
            return

        for i in range(idx, len(nums)):
            self.track.append(nums[i])
            self.backTrack(nums, i, cur + nums[i])
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.backTrack(candidates, 0, 0)
        return self.ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
