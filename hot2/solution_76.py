class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        valid = 0
        i, j = 0, 0
        start = -1
        length = len(s) + 1

        while j < len(s):
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
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window[d] - 1
                i += 1
        return s[start: start + length] if start >= 0 else ''


# result = Solution().minWindow('ADOBECODEBANC', 'ABC')
# result = Solution().minWindow('a', 'aa')
result = Solution().minWindow('a', 'a')
print(result)
