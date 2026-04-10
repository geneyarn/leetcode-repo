from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)

        track = []
        ans = []

        def backTrack(idx: int):
            ans.append(track.copy())

            for i in range(idx, m):
                track.append(nums[i])
                backTrack(i + 1)
                track.pop()

        backTrack(0)
        return ans


result = Solution().subsets([1, 2, 3])
print(result)
