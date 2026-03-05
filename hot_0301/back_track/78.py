from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []

    def backTrack(self, nums: List[int], idx: int):
        self.ans.append(self.track.copy())
        if idx == len(nums):
            return

        for i in range(idx, len(nums)):
            self.track.append(nums[i])
            self.backTrack(nums, i + 1)
            self.track.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        self.backTrack(nums, 0)
        return self.ans


result = Solution().subsets([1, 2, 3])
print(result)
