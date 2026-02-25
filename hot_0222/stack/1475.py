from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m = len(prices)

        ans = [0] * m
        stk = []

        for i in range(m - 1, -1, -1):
            while stk and stk[-1] > prices[i]:
                stk.pop()

            ans[i] = prices[i] if not stk else prices[i] - stk[-1]
            stk.append(prices[i])

        return ans


# result = Solution().finalPrices([8, 4, 6, 2, 3])
result = Solution().finalPrices([10, 1, 1, 6])
print(result)
