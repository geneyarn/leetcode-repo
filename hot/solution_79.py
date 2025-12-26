from typing import List


class Solution:

    def __init__(self):
        self.visited = []

    def backTrack(self, board: List[List[str]], i: int, j: int, word: str, cur: int) -> bool:
        if cur >= len(word):
            return True
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if self.visited[i][j]:
            return False
        if board[i][j] != word[cur]:
            return False

        self.visited[i][j] = True
        ans = (self.backTrack(board, i - 1, j, word, cur + 1)
               or self.backTrack(board, i + 1, j, word, cur + 1)
               or self.backTrack(board, i, j - 1, word, cur + 1) or
               self.backTrack(board, i, j + 1, word, cur + 1))
        self.visited[i][j] = False
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.backTrack(board, i, j, word, 0):
                    return True
        return False
