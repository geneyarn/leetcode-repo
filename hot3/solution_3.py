class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)

        ans = 0

        charMp = {}
        i, j = 0, 0

        while j < m:
            c = s[j]
            j += 1
            charMp[c] = charMp.get(c, 0) + 1

            while j - i > len(charMp.keys()):
                d = s[i]
                charMp[d] = charMp[d] - 1
                if charMp[d] == 0:
                    charMp.pop(d)
                i += 1

            ans = max(ans, j - i)
        return ans


result = Solution().lengthOfLongestSubstring('abcabcbb')
print(result)
