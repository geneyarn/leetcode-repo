from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        used = [[False] * n for _ in range(m)]

        def backTrack(idx: int, i: int, j: int):
            if idx == len(word):
                return True
            nonlocal used

            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if used[i][j]:
                return False

            if board[i][j] != word[idx]:
                return False
            used[i][j] = True
            ans = backTrack(idx + 1, i + 1, j) or backTrack(idx + 1, i - 1, j) or backTrack(idx + 1, i,
                                                                                            j + 1) or backTrack(
                idx + 1, i, j - 1)
            used[i][j] = False

            return ans

        for k in range(m):
            for l in range(n):
                ans = backTrack(0, k, l)
                if ans:
                    return True

        return False


# result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED')
result = Solution().exist([
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]], 'AAB')
print(result)
