from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            pre = res[-1]
            cur = intervals[i]

            if pre[1] >= cur[0]:
                pre[1] = max(cur[1], pre[1])
            else:
                res.append(cur)

        return res
