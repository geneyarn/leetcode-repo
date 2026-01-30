from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        windowMp = {}
        validCount = 0
        ans = []
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            j += 1
            if c in need:
                windowMp[c] = windowMp.get(c, 0) + 1
                if windowMp[c] == need[c]:
                    validCount += 1

            while j - i > len(p):
                d = s[i]
                if d in need:
                    if windowMp[d] == need[d]:
                        validCount -= 1
                    windowMp[d] = windowMp[d] - 1
                i += 1

            if validCount == len(need.keys()):
                ans.append(i)

        return ans


result = Solution().findAnagrams('cbaebabacd', 'abc')
print(result)
