class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, 27):
            res = max(res, self.longestSubStringWithLen(s, k, i))

        return res

    def longestSubStringWithLen(self, s: str, k: int, j: int) -> int:
        res = 0
        mp = {}
        left, right = 0, 0
        validCharCount = 0

        while right < len(s):
            c = s[right]
            right += 1
            mp[c] = mp.get(c, 0) + 1
            if mp[c] == k:
                validCharCount += 1

            while len(mp.keys()) > j:
                d = s[left]
                if mp[d] == k:
                    validCharCount -= 1
                mp[d] = mp[d] - 1
                if mp[d] == 0:
                    mp.pop(d)
                left += 1
            if validCharCount == len(mp.keys()):
                res = max(res, right - left)

        return res


# result = Solution().longestSubstring('aaabb', 3)
# result = Solution().longestSubstring('ababbc', 2)
result = Solution().longestSubstring('bbaaacbd', 3)
print(result)
