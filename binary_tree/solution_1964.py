from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stk = [0] * len(obstacles)
        result = []
        cur = 0

        for n in obstacles:
            l, r = 0, cur
            while l < r:
                mid = (l + r) // 2
                if stk[mid] <= n:
                    l = mid + 1
                else:
                    r = mid
            if l == cur:
                cur += 1
            stk[l] = n
            result.append(l + 1)

        return result


result = Solution().longestObstacleCourseAtEachPosition([1, 2, 3, 2])
# result = Solution().longestObstacleCourseAtEachPosition([2, 2, 1])
# result = Solution().longestObstacleCourseAtEachPosition([5, 1, 5, 5, 1, 3, 4, 5, 1, 4])
print(result)
