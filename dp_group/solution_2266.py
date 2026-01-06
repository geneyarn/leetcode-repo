from itertools import groupby


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 1_000_000_007
        f = [1, 1, 2, 4]
        g = [1, 1, 2, 4]
        for _ in range(10 ** 5 - 3):  # 预处理所有长度的结果
            f.append((f[-1] + f[-2] + f[-3]) % MOD)
            g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

        ans = 1
        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if ch in "79" else f[m]) % MOD
        return ans


result = Solution().countTexts('22233')
print(result)

# 2 a
# 22 aa b
# 222 aaa ba ab c
# 2222 aaaa baa aba aab bb ac ca
