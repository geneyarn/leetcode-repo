from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        window = {}
        valid = 0
        i, j = 0, 0
        ans = []
        while j < m:
            c = s[j]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            j += 1

            while j - i > len(p):
                d = s[i]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window[d] - 1
                i += 1

            if valid == len(need):
                ans.append(i)
        return ans


# result = Solution().findAnagrams('cbaebabacd', 'abc')
result = Solution().findAnagrams('abaacbabc', 'abc')
# result = Solution().findAnagrams('baa', 'aa')
print(result)
