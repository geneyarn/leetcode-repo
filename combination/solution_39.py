from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def backTrack(self, nums: List[int], idx: int, target: int, track: List[int]):
        if target < 0:
            return
        if target == 0:
            self.ans.append(track.copy())
            return

        for i in range(idx, len(nums)):
            target -= nums[i]
            track.append(nums[i])
            self.backTrack(nums, i, target, track)
            track.pop()
            target += nums[i]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backTrack(candidates, 0, target, [])

        return self.ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
