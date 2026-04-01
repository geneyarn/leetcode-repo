from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1

            key = '-'.join([str(t) for t in arr])
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]

        return mp.values()
