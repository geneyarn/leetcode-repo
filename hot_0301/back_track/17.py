from typing import List


class Solution:

    def __init__(self):
        self.mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        self.ans = []
        self.track = []

    def backTrack(self, digits: str, idx: int):
        if idx == len(digits):
            self.ans.append(''.join(self.track))
            return

        n = digits[idx]
        for c in self.mp[n]:
            self.track.append(c)
            self.backTrack(digits, idx + 1)
            self.track.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.backTrack(digits, 0)
        return self.ans


result = Solution().letterCombinations('23')
print(result)
