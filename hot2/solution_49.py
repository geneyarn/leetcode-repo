from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord('a')] += 1
            key = ','.join([str(c) for c in a])
            if key not in mp:
                mp[key] = [s]
            else:
                mp[key].append(s)
        res = []
        for value in mp.values():
            res.append(value)

        return res


result = Solution().groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"])
print(result)
