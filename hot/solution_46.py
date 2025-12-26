class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needMp = {}
        for c in t:
            needMp[c] = needMp.get(c, 0) + 1

        res = float('inf')
        left = -1
        window = {}
        validCount = 0
        l, r = 0, 0

        while r < len(s):
            c = s[r]
            r += 1
            if c in needMp:
                window[c] = window.get(c, 0) + 1
                if window[c] == needMp[c]:
                    validCount += 1

            while validCount == len(needMp.keys()):
                if res > r - l:
                    left = l
                    res = r - l
                d = s[l]
                if d in needMp:
                    if window[d] == needMp[d]:
                        validCount -= 1
                    window[d] = window[d] - 1

                l += 1

        return s[left:left + res] if res != float('inf') else ''


result = Solution().minWindow('ADOBECODEBANC', 'ABC')
print(result)
