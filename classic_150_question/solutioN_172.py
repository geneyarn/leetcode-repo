class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n > 0:
            n = n // 5
            ans += 1
        return ans


result = Solution().trailingZeroes(5)
result = Solution().trailingZeroes(5)
print(result)
