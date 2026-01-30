from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        m = len(candidates)
        ans = []
        track = []

        def backTrack(idx: int, t: int):
            if t > target:
                return
            if t == target:
                ans.append(track.copy())
                return

            for i in range(idx, m):
                track.append(candidates[i])
                backTrack(i, t + candidates[i])
                track.pop()

        backTrack(0, 0)

        return ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
