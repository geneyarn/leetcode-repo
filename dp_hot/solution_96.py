from functools import cache


class Solution:

    @cache
    def get_count(self, left: int, right: int) -> int:
        if left >= right:
            return 1

        ans = 0
        for i in range(left, right + 1):
            l = self.get_count(left, i - 1)
            r = self.get_count(i + 1, right)
            ans += (l * r)

        return ans

    def numTrees(self, n: int) -> int:

        return self.get_count(1, n)


result = Solution().numTrees(3)
print(result)
