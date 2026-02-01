class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            t = mid * mid
            if t == x:
                return mid
            if t > x:
                r = mid - 1
            else:
                l = mid + 1
        return r


# result = Solution().mySqrt(4)
# result = Solution().mySqrt(5)
result = Solution().mySqrt(8)
print(result)
