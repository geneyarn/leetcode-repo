class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        mp = {}
        res = 0
        while j < len(s):
            c = s[j]
            mp[c] = mp.get(c, 0) + 1
            j += 1

            while mp[c] > 1:
                d = s[i]
                mp[d] = mp[d] - 1
                i += 1

            res = max(j - i, res)

        return res


result = Solution().lengthOfLongestSubstring('bbbbb')
print(result)
