from typing import List


class Solution:

    def __init__(self):
        self.count = 0
        self.ans = []

    def backTrack(self, nums: List[int], idx: int, target: int, track: List[int]):
        if len(track) > self.count:
            return
        if len(track) == self.count and target == 0:
            self.ans.append(track.copy())
            return

        for i in range(idx, len(nums)):
            target -= nums[i]
            track.append(nums[i])
            self.backTrack(nums, i + 1, target, track)
            track.pop()
            target += nums[i]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.count = k
        self.backTrack(arr, 0, n, [])

        return self.ans


result = Solution().combinationSum3(3, 9)
print(result)
