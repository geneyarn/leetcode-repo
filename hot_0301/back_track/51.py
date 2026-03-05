from typing import List


class Solution:

    def __init__(self):
        self.grid = []
        self.ans = []

    def valid(self, row: int, col: int) -> bool:
        for r in range(len(self.grid)):
            if self.grid[r][col] == 'Q':
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if self.grid[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < len(self.grid):
            if self.grid[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backTrack(self, idx: int):
        if idx == len(self.grid):
            self.ans.append([''.join(s) for s in self.grid])
            return

        for i in range(len(self.grid)):
            if self.valid(idx, i):
                self.grid[idx][i] = 'Q'
                self.backTrack(idx + 1)
                self.grid[idx][i] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.grid = [['.'] * n for _ in range(n)]
        self.backTrack(0)
        return self.ans


result = Solution().solveNQueens(4)
print(result)
