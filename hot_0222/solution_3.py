class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)
        if m == 0:
            return 0

        i, j = 0, 0
        window = {}

        ans = 1
        while j < m:
            c = s[j]
            window[c] = window.get(c, 0) + 1
            j += 1

            while window[c] > 1:
                d = s[i]
                window[d] -= 1
                i += 1

            ans = max(ans, j - i)
        return ans


result = Solution().lengthOfLongestSubstring('abcabcbb')
print(result)
