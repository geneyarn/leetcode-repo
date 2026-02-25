from typing import List


class Solution:

    def __init__(self):
        self.track = []
        self.ans = []

    def backTrack(self, nums: List[int], idx: int):
        self.ans.append(self.track.copy())

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue

            self.track.append(nums[i])
            self.backTrack(nums, i + 1)
            self.track.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backTrack(nums, 0)
        return self.ans


result = Solution().subsetsWithDup([1, 2, 2])
print(result)
