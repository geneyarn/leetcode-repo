from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        pathSet = set()

        def backTrack(i: int, j: int, idx: int) -> bool:
            if idx >= len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[idx]:
                return False
            key = f'{i}-{j}'
            if key in pathSet:
                return False

            pathSet.add(key)
            ans = (backTrack(i + 1, j, idx + 1)
                   or backTrack(i - 1, j, idx + 1)
                   or backTrack(i, j + 1, idx + 1)
                   or backTrack(i, j - 1, idx + 1))
            pathSet.remove(key)
            return ans

        for i in range(m):
            for j in range(n):
                if backTrack(i, j, 0):
                    return True
        return False


result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED')
print(result)
