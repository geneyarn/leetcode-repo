from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = len(arr)
        dp = [1] * m
        mp = {arr[0]: 0}

        for i in range(1, m):
            if arr[i] - difference in mp:
                dp[i] = dp[mp[arr[i] - difference]] + 1
            mp[arr[i]] = i

        return max(dp)


result = Solution().longestSubsequence([1, 2, 3, 4], 1)
# result = Solution().longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2)
print(result)
