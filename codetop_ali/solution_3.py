class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)
        window = {}

        i, j = 0, 0

        result = 0

        while j < m:
            c = s[j]
            j += 1
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[i]
                i += 1
                window[d] = window[d] - 1
            result = max(result, j - i)

        return result


# result = Solution().lengthOfLongestSubstring('abcabcbb')
# result = Solution().lengthOfLongestSubstring('bbbbb')
result = Solution().lengthOfLongestSubstring('pwwkew')
print(result)
