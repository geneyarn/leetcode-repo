from itertools import groupby


class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        MOD = 1_000_000_007
        three = [1] * (10 ** 5 + 1)
        four = [1] * (10 ** 5 + 1)

        three[1], three[2], three[3] = 1, 2, 4
        four[1], four[2], four[3] = 1, 2, 4

        for i in range(4, 10 ** 5 + 1):
            three[i] = (three[i - 1] + three[i - 2] + three[i - 3]) % MOD
            four[i] = (four[i - 1] + four[i - 2] + four[i - 3] + four[i - 4]) % MOD

        ans = 1
        for c, l in groupby(pressedKeys):
            m = len(list(l))
            ans *= (four[m] if c in '79' else three[m]) % MOD

        return ans


result = Solution().countTexts('22233')
print(result)
