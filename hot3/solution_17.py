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

    def traverse(self, digits: str, idx: int, track: List[str]):
        if idx == len(digits):
            self.ans.append(''.join(track))
            return

        for c in self.mp[digits[idx]]:
            track.append(c)
            self.traverse(digits, idx + 1, track)
            track.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.traverse(digits, 0, [])
        return self.ans
