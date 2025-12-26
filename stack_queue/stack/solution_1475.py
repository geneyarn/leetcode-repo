from typing import List


# 给你一个数组prices ，其中prices[i]是商店里第i件商品的价格。商店里正在进行促销活动，如果你要买第i件商品，那么你可以得到与prices[j]相等的折扣，其中
# j是满足j > i且prices[j] <= prices[i]的最小下标 ，如果没有满足条件的j ，你将没有任何折扣。请你返回一个数组，数组中第i个元素是折扣后你购买商品i最终需要支付的价格。
#
# 输入：prices = [8, 4, 6, 2, 3]
# 输出：[4, 2, 4, 2, 3]
# 输入：prices = [1, 2, 3, 4, 5]
# 输出：[1, 2, 3, 4, 5]
# 输入：prices = [10, 1, 1, 6]
# 输出：[9, 0, 1, 6]

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m = len(prices)
        stk = []
        res = [0] * m
        for i in range(m - 1, -1, -1):
            while stk and stk[-1] > prices[i]:
                stk.pop()
            res[i] = prices[i] if not stk else prices[i] - stk[-1]
            stk.append(prices[i])
            
        return res


result = Solution().finalPrices([8, 4, 6, 2, 3])
print(result)
