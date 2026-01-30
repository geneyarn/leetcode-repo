from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def traverse(self, nums: List[int], idx: int, need: int, track: List[int]):
        if need < 0:
            return
        if need == 0:
            self.ans.append(track.copy())
            return

        for i in range(idx, len(nums)):
            track.append(nums[i])
            self.traverse(nums, i, need - nums[i], track)
            track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.traverse(candidates, 0, target, [])
        return self.ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
