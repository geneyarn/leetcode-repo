from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        i, j = 0, 0
        window = {}
        valid = 0
        ans = []

        while j < m:
            c = s[j]
            j += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while j - i > n:
                d = s[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window[d] - 1

            if valid == len(need.keys()):
                ans.append(i)
        return ans


result = Solution().findAnagrams('cbaebabacd', 'abc')
print(result)
