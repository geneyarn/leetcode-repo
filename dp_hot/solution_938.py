from functools import cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mp = {value: idx for idx, value in enumerate(days)}
        mx = max(days)

        @cache
        def dfs(num: int) -> int:
            if num <= 0:
                return 0
            if num not in mp:
                return dfs(num - 1)

            return min(dfs(num - 1) + costs[0], dfs(num - 7) + costs[1], dfs(num - 30) + costs[2])

        return dfs(mx)


result = Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
print(result)
