class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = len(s)
        maxCharCount = 0
        res = 0

        left, right = 0, 0
        mp = {}
        while right < m:
            c = s[right]
            mp[c] = mp.get(c, 0) + 1
            right += 1
            maxCharCount = max(maxCharCount, mp[c])

            while left < right and right - left - maxCharCount > k:
                d = s[left]
                mp[d] = mp[d] - 1
                left += 1

            res = max(res, right - left)

        return res


result = Solution().characterReplacement('ABAB', 2)
print(result)
