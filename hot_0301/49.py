from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = len(strs)
        mp = {}

        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1

            key = '-'.join([str(t) for t in tmp])
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]

        return list(mp.values())
