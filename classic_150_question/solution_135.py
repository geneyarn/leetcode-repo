from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        m = len(ratings)
        left = [1] * m
        ans = 0
        for i in range(1, m):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        right = [1] * m
        ans += max(left[-1], right[-1])
        for j in range(m - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right[j] = right[j + 1] + 1
            ans += max(left[j], right[j])
        return ans


# result = Solution().candy([1, 0, 2])
result = Solution().candy([1, 2, 2])
print(result)
