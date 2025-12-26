from typing import List


class Solution:

    def leftBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = {}

        for i in range(len(s)):
            c = s[i]
            if c in mp:
                mp[c].append(i)
            else:
                mp[c] = [i]

        i, j = 0, 0

        res = 0

        for i in range(len(words)):
            w = words[i]

            i, j = 0, 0

            while i < len(w):
                c = w[i]
                if c not in mp:
                    break
                indexList = mp.get(c)
                idx = self.leftBound(indexList, j)
                if idx < 0 or idx >= len(indexList):
                    break
                j = indexList[idx]
                i += 1
                j += 1
            if i == len(w):
                res += 1
        return res


result = Solution().numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"])
print(result)
