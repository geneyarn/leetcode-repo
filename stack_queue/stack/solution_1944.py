from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        m = len(heights)
        res = [0] * m
        stk = []

        for i in range(m - 1, -1, -1):
            count = 0
            while stk and stk[-1] < heights[i]:
                stk.pop()
                count += 1

            res[i] = count if not stk else count + 1
            stk.append(heights[i])
        return res


result = Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9])
print(result)
# [3,1,2,1,1,0]
