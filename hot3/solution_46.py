from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        used = [False] * m

        ans = []

        def traverse(track: List[int]):
            if len(track) == m:
                ans.append(track.copy())
                return

            for i in range(m):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                traverse(track)
                used[i] = False
                track.pop()

        traverse([])
        return ans


result = Solution().permute([1, 2, 3])
print(result)
