from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        needMp = {}
        for c in p:
            needMp[c] = needMp.get(c, 0) + 1

        valid = 0
        i, j = 0, 0
        window = {}
        res = []
        while j < len(s):
            c = s[j]
            j += 1

            if c in needMp:
                window[c] = window.get(c, 0) + 1
                if window[c] == needMp[c]:
                    valid += 1

            while j - i > len(p):
                d = s[i]
                i += 1
                if d in needMp:
                    if window[d] == needMp[d]:
                        valid -= 1
                    window[d] = window[d] - 1

            if valid == len(needMp.keys()):
                res.append(i)

        return res


result = Solution().findAnagrams('cbaebabacd', 'abc')
print(result)
