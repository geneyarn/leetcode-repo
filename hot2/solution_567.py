class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, 0
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        mp = {}
        validSize = 0

        while j < len(s2):
            c = s2[j]
            j += 1
            if c in need:
                mp[c] = mp.get(c, 0) + 1
                if mp[c] == need[c]:
                    validSize += 1

            while j - i > len(s1):
                d = s2[i]
                if d in need:
                    if mp[d] == need[d]:
                        validSize -= 1
                    mp[d] = mp[d] - 1
                i += 1

            if validSize == len(need):
                return True
        return False


# result = Solution().checkInclusion('ab', 'eidboaoo')
result = Solution().checkInclusion('abc', 'ccccbbbbaaaa')
print(result)
