from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i, j = 0, 0
        res = []
        mp = {}

        need = {}
        validCount = 0
        for c in p:
            need[c] = need.get(c, 0) + 1

        while j < len(s):
            c = s[j]
            j += 1
            if c in need:
                mp[c] = mp.get(c, 0) + 1
                if need[c] == mp[c]:
                    validCount += 1

            while j - i > len(p):
                d = s[i]
                if d in need:
                    if mp[d] == need[d]:
                        validCount -= 1
                    mp[d] = mp[d] - 1
                i += 1
            if validCount == len(need.keys()):
                res.append(i)

        return res


result = Solution().findAnagrams('cbaebabacd', 'abc')
print(result)
