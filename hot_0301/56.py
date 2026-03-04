from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = len(intervals)

        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = [intervals[0]]

        for i in range(1, m):
            last = ans[-1]
            cur = intervals[i]

            if last[1] >= cur[0]:
                last[1] = max(cur[1], last[1])
            else:
                ans.append(cur)

        return ans


result = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(result)
