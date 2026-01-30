class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        m = len(s)
        i, j = 0, 0
        window = {}
        start = -1
        length = m + 1
        validCount = 0

        while j < m:
            c = s[j]
            j += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    validCount += 1

            while validCount == len(need.keys()):
                if j - i < length:
                    start = i
                    length = j - i

                d = s[i]
                if d in need:
                    if window[d] == need[d]:
                        validCount -= 1
                    window[d] = window[d] - 1
                i += 1

        return s[start: start + length] if start >= 0 else ""
