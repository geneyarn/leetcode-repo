from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = len(arr)

        mp = {arr[0]: 0}
        dp = [1] * m
        for i in range(m):
            if arr[i] - difference in mp:
                dp[i] = dp[mp[arr[i] - difference]] + 1
            mp[arr[i]] = i

        return max(dp)


result = Solution().longestSubsequence([1, 2, 3, 4], 1)
print(result)
