from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        arr = []
        for v in envelopes:
            arr.append(v[1])
        m = len(arr)
        pies = [0] * m
        cur = 0

        for n in arr:
            l, r = 0, cur
            while l < r:
                mid = (l + r) // 2
                if pies[mid] >= n:
                    r = mid
                else:
                    l = mid + 1
            if l == cur:
                cur += 1
            pies[l] = n
        return cur


result = Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
print(result)
