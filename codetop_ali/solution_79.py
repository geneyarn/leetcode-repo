from typing import List


class Solution:

    def __init__(self):
        self.track = set()

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backTrack(i: int, j: int, idx: int) -> bool:
            if idx >= len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[idx]:
                return False
            key = f"{i}-{j}"
            if key in self.track:
                return False

            self.track.add(key)

            ans = ((backTrack(i - 1, j, idx + 1)
                    or backTrack(i + 1, j, idx + 1)
                    or backTrack(i, j + 1, idx + 1))
                   or backTrack(i, j - 1, idx + 1))
            self.track.remove(key)

            return ans

        ans = False
        for i in range(m):
            for j in range(n):
                if ans:
                    break
                self.track = set()
                ans = backTrack(i, j, 0)

        return ans


# result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED')
# result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCEDB')
# result = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB')
# result = Solution().exist([['a']], 'a')
result = Solution().exist([["A", "B", "C", "E"],
                           ["S", "F", "E", "S"],
                           ["A", "D", "E", "E"]], 'ABCESEEEFS')
print(result)
