from cmath import inf
from typing import List


class Solution:
    def __init__(self):
        self.countMp = {}
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])

        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return -inf

            if i == m - 1 and j == n - 1:
                return 0

            s = board[i]
            c = s[j]
            if c == 'X':
                return -inf

            ans = int(c) if c.isdigit() else 0
            tmp = max(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1)) + ans

            if 0 < (i + j) <= 2:
                self.countMp[tmp] = self.countMp.get(tmp, 0) + 1
            print(f'{i}---{j}---{tmp}')
            return tmp

        big = dp(0, 0)
        if big > -inf:
            count = self.countMp.get(big, 1)

            return [big, (count) % (10 ** 9 + 7)]
        else:
            return [0, 0]


# result = Solution().pathsWithMaxScore(["E23",
#                                        "2X2",
#                                        "12S"])
# result = Solution().pathsWithMaxScore(["E12",
#                                        "1X1",
#                                        "21S"])
# result = Solution().pathsWithMaxScore(["E11",
#                                        "XXX",
#                                        "11S"])
# result = Solution().pathsWithMaxScore(["EX",
#                                        "XS"])
result = Solution().pathsWithMaxScore(["E11345", "X452XX", "3X43X4", "422812", "284522", "13422S"]
                                      )
print(result)
