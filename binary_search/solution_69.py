class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2
            v = mid * mid
            if v == x:
                return mid
            if v > x:
                r = mid - 1
            else:
                l = mid + 1
        return r

# result = Solution().mySqrt(8)
result = Solution().mySqrt(4)
print(result)