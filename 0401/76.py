from cmath import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        valid = 0
        start = -1
        length = inf

        i, j = 0, 0

        while j < len(s):
            c = s[j]
            j += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if length > j - i:
                    start = i
                    length = j - i

                d = s[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start:start + length] if length < inf else ""


result = Solution().minWindow('ADOBECODEBANC', 'ABC')
print(result)
