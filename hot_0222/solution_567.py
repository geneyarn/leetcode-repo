class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s2)
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}
        valid = 0
        i, j = 0, 0

        while j < m:
            c = s2[j]
            j += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while j - i > len(s1):
                d = s2[i]
                i += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
            if valid == len(need):
                return True

        return False


# result = Solution().checkInclusion('ab', 'eidbaooo')
result = Solution().checkInclusion('ab', 'eidboaoo')
print(result)
