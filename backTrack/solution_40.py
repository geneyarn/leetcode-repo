from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []
        self.targetSum = 0

    def backTrack(self, candidates: List[int], target: int, start: int):
        if self.targetSum == target:
            self.ans.append(self.track.copy())
            return
        if self.targetSum > target:
            return

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            self.targetSum += candidates[i]
            self.track.append(candidates[i])
            self.backTrack(candidates, target, i + 1)
            self.track.pop()
            self.targetSum -= candidates[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backTrack(candidates, target, 0)
        return self.ans


result = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(result)
