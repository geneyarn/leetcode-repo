from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        arr = [0] * len(hours)
        for i in range(len(hours)):
            arr[i] = (1 if hours[i] > 8 else -1)

        i, j = 0, 0
        curSum = 0
        res = 0

        while j < len(hours):
            val = arr[j]
            j += 1

            curSum += val

            while i < j and curSum < -1:
                left = arr[i]
                curSum -= left
                i += 1

            if curSum > 0:
                res = max(res, j - i)
        return res

    def longestWPI2(self, hours: List[int]) -> int:
        m = len(hours)

        preSum = [0] * (m + 1)
        for i in range(1, m + 1):
            preSum[i] = preSum[i - 1] + (1 if hours[i - 1] > 8 else -1)

        val2IdxMp = {}
        res = 0
        for i in range(1, m + 1):
            if preSum[i] not in val2IdxMp:
                val2IdxMp[preSum[i]] = i
            if preSum[i] > 0:
                res = max(res, i)
            else:
                if preSum[i] - 1 in val2IdxMp:
                    res = max(res, i - val2IdxMp[preSum[i] - 1])

        return res


# result = Solution().longestWPI([9, 9, 6, 0, 6, 6, 9])
result = Solution().longestWPI([6, 6, 9])
print(result)
