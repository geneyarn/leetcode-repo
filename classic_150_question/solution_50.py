class Solution:

    def quickMulti(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        half = self.quickMulti(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x

    def myPow(self, x: float, n: int) -> float:
        return self.quickMulti(x, n) if n > 0 else 1.0 / self.quickMulti(x, -n)


# result = Solution().myPow(2, 10)
# result = Solution().myPow(2.1, 3)
result = Solution().myPow(2, -2)
print(result)
