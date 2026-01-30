from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]
            cur = intervals[i]

            if cur[0] > last[1]:
                result.append(cur)
            else:
                last[1] = max(last[1], cur[1])
        return result
