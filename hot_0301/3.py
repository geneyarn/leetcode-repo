class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)
        i, j = 0, 0

        mp = {}
        ans = 0
        while j < m:
            c = s[j]
            j += 1

            mp[c] = mp.get(c, 0) + 1

            while mp[c] > 1:
                d = s[i]
                i += 1
                mp[d] = mp[d] - 1
            ans = max(ans, j - i)
        return ans


result = Solution().lengthOfLongestSubstring('abcabcbb')
print(result)
