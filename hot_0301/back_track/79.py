from typing import List


class Solution:

    def __init__(self):
        self.used = []

    def backTrack(self, board: List[List[str]], i: int, j: int, word: str, idx: int) -> bool:

        if idx == len(word):
            return True

        if i < 0 or i >= len(board):
            return False
        if j < 0 or j >= len(board[i]):
            return False

        if self.used[i][j]:
            return False

        if board[i][j] != word[idx]:
            return False
        self.used[i][j] = True
        ans = (self.backTrack(board, i + 1, j, word, idx + 1) or
               self.backTrack(board, i - 1, j, word, idx + 1) or
               self.backTrack(board, i, j + 1, word, idx + 1) or
               self.backTrack(board, i, j - 1, word, idx + 1))

        self.used[i][j] = False

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.used = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = self.backTrack(board, i, j, word, 0)
                if ans:
                    return True
        return False


result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED1')
print(result)
