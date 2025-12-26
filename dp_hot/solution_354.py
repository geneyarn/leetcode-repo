from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        arr = []
        for kv in envelopes:
            arr.append(kv[1])

        stk = [0] * len(arr)
        cur = 0
        for n in arr:
            l, r = 0, cur
            while l < r:
                mid = (l + r) // 2
                if stk[mid] >= n:
                    r = mid
                else:
                    l = mid + 1
            if l == cur:
                cur += 1
            stk[l] = n

        return cur

        # m = len(arr)
        # dp = [1] * m
        # for i in range(1, m):
        #     for j in range(i):
        #         if arr[j] < arr[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)


result = Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
print(result)
