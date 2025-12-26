from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = [envelopes[i][1] for i in range(len(envelopes))]

        top = [0] * len(height)
        pile = 0

        for n in height:
            i, j = 0, pile

            while i < j:
                mid = (i + j) // 2
                if top[mid] >= n:
                    j = mid
                else:
                    i = mid + 1

            if j == pile:
                pile += 1

            top[j] = n
        return pile


result = Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
print(result)
