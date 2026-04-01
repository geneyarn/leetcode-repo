class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)

        ans = 0
        window = {}

        i, j = 0, 0

        while j < m:
            c = s[j]
            j += 1

            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[i]
                window[d] = window[d] - 1
                i += 1

            ans = max(j - i, ans)
        return ans


result = Solution().lengthOfLongestSubstring('abcabcbb')
print(result)
