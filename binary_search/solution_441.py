import math



class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0, n

        while l <= r:
            mid = (l + r) // 2
            if mid * (mid + 1) > 2 * n:
                r = mid - 1
            else:
                l = mid + 1
        return r

result = Solution().arrangeCoins(5)
# result = Solution().arrangeCoins(8)
print(result)
