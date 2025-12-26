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
            if i > idx and nums[i] == nums[i - 1]:
                continue
            target -= nums[i]
            track.append(nums[i])
            self.backTrack(nums, i + 1, target, track)
            track.pop()
            target += nums[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backTrack(candidates, 0, target, [])

        return self.ans


result = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(result)
