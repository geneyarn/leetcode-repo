from typing import List


class Solution:

    def __init__(self):
        self.board: List[List[str]] = []
        self.used = []
        self.word: str = ''
        self.track = []

    def backTrack(self, i: int, j: int, idx: int) -> bool:
        if idx == len(self.word):
            return True
        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]):
            return False

        if self.used[i][j]:
            return False

        if self.board[i][j] != self.word[idx]:
            return False

        self.used[i][j] = True

        ans = (self.backTrack(i + 1, j, idx + 1)
               or self.backTrack(i - 1, j, idx + 1)
               or self.backTrack(i, j + 1, idx + 1) or self.backTrack(i, j - 1, idx + 1))
        self.used[i][j] = False
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.board = board
        self.used = [[False] * n for _ in range(m)]
        self.word = word

        for i in range(m):
            for j in range(n):
                ans = self.backTrack(i, j, 0)
                if ans:
                    return True

        return False


# result = Solution().exist([['A', 'B', 'C', 'E'],
#                            ['S', 'F', 'C', 'S'],
#                            ['A', 'D', 'E', 'E']], 'ABCCED')
# result = Solution().exist([['A', 'B', 'C', 'E'],
#                            ['S', 'F', 'C', 'S'],
#                            ['A', 'D', 'E', 'E']], 'ABCB')
result = Solution().exist([
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]],
    'AAB')
print(result)
