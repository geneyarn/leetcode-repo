from typing import List


class Solution:

    def __init__(self):
        self.target = 0
        self.ans = []

    def backTrack(self, candidates: List[int], track: List[int], curSum: int, idx: int):
        if curSum > self.target:
            return
        if curSum == self.target:
            self.ans.append(track.copy())
            return

        for i in range(idx, len(candidates)):
            track.append(candidates[i])
            self.backTrack(candidates, track, curSum + candidates[i], i)
            track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.backTrack(candidates, [], 0, 0)
        return self.ans
