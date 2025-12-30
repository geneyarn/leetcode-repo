class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', '0'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '0': ['w', 'x', 'y', 'z']
        }

        m = len(pressedKeys)


result = Solution().countTexts('22233')
print(result)
