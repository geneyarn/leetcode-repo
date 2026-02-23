from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        start = -1
        length = inf
        valid = 0
        i, j = 0, 0
        while j < m:
            c = s[j]
            j += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if j - i < length:
                    start = i
                    length = j - i
                d = s[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window[d] - 1

        return s[start:start + length] if start >= 0 else ''


result = Solution().minWindow('ADOBECODEBANC', 'ABC')
print(result)
