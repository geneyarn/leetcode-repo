from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        m = len(candidates)
        ans = []

        def backTrack(idx: int, cur: int, track: list[int]):
            nonlocal ans
            if idx >= m:
                return

            if cur > target:
                return
            if cur == target:
                ans.append(track.copy())
                return

            for i in range(idx, m):
                cur += candidates[i]
                track.append(candidates[i])
                backTrack(i, cur, track)
                cur -= candidates[i]
                track.pop()

        backTrack(0, 0, [])
        return ans


result = Solution().combinationSum([2, 3, 6, 7], 7)
print(result)
