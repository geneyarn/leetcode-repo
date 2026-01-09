from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        dp = [0] * len(cuboids)

        result = 0
        for i in range(len(cuboids)):
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j])

            dp[i] += cuboids[i][2]
            result = max(dp[i], result)
        return result


result = Solution().maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]])
# result = Solution().maxHeight([[38, 25, 45], [76, 35, 3]])
print(result)
