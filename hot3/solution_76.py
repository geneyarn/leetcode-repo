class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        valid = 0
        start, length = -1, len(s) + 1
        window = {}
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            j += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need.keys()):
                if j - i < length:
                    start = i
                    length = j - i

                d = s[i]
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
                i += 1

        return "" if start == -1 else s[start: start + length]


# result = Solution().minWindow('ADOBECODEBANC', 'ABC')
result = Solution().minWindow('a', 'a')
print(result)
