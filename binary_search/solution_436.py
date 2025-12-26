from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        m = len(intervals)
        mp = {v[0]: i for i, v in enumerate(intervals)}
        startArr = [x[0] for x in intervals]
        startArr.sort()

        result = [-1] * len(intervals)

        for i in range(m):
            if i + 1 < m:
                result[mp.get(startArr[i])] = mp.get(startArr[i + 1])

        return result


# result = Solution().findRightInterval([[3, 4], [2, 3], [1, 2]])
result = Solution().findRightInterval([[1, 4], [2, 3], [3, 4]])
print(result)
