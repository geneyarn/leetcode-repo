from typing import List


class Solution:

    def getHousrs(self, piles: List[int], speed: int) -> int:
        res = 0
        for n in piles:
            if n < speed:
                res += 1
            else:
                res += (n // speed) + (1 if n % speed > 0 else 0)

        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 10 ** 9 + 1

        while left < right:
            mid = left + (right - left) // 2
            tmp = self.getHousrs(piles, mid)
            if tmp <= h:
                right = mid
            else:
                left = mid + 1

        return left


# result = Solution().getHousrs([3, 6, 7, 11], 4)
# result = Solution().minEatingSpeed([3, 6, 7, 11], 8)
result = Solution().minEatingSpeed([30, 11, 23, 4, 20], 5)
print(result)
