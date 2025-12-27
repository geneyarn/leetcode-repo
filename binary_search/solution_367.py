import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = (l + r) // 2
            p = math.pow(mid, 2)
            if p == num:
                return True
            if p < num:
                l = mid + 1
            else:
                r = mid - 1
        return False