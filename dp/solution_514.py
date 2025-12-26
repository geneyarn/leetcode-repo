class Solution:
    # 字符 -> 索引列表
    def __init__(self):
        self.charToIndex = {}
        # 备忘录
        self.memo = []

    def dp(self, ring: str, i: int, key: str, j: int) -> int:
        if j == len(key):
            return 0

        n = len(ring)
        res = float('inf')
        if self.memo[i][j] != 0:
            return self.memo[i][j]

        for c in self.charToIndex[key[j]]:
            delta = min(abs(c - i), n - abs(c - i))
            sub = self.dp(ring, c, key, j + 1)

            res = min(res, sub + 1 + delta)

        self.memo[i][j] = res
        return res

    # 主函数
    def findRotateSteps2(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)
        # 备忘录全部初始化为 0
        self.memo = [[0] * n for _ in range(m)]
        for idx, c in enumerate(ring):
            if c not in self.charToIndex:
                self.charToIndex[c] = [idx]
            else:
                self.charToIndex[c].append(idx)
        return self.dp(ring, 0, key, 0)

    def findRotateSteps(self, ring: str, key: str) -> int:
        for idx, c in enumerate(ring):
            if c not in self.charToIndex:
                self.charToIndex[c] = [idx]
            else:
                self.charToIndex[c].append(idx)

        pass


result = Solution().findRotateSteps2('godding', 'gd')
print(result)
