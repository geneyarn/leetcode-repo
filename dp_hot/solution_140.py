from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ws = set(wordDict)
        m = len(s)

        ans = []

        def backTrack(idx: int, track: List[str]):
            if idx == m:
                ans.append(' '.join(track))
                return

            for i in range(idx, m + 1):
                sub = s[idx:i]
                if sub in ws:
                    track.append(sub)
                    backTrack(i, track)
                    track.pop()

        backTrack(0, [])
        return ans


result = Solution().wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
print(result)
