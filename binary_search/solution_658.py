from typing import List


class Solution:

    def leftBound(self, arr: List[int], target: int) -> int:
        m = len(arr)
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = self.leftBound(arr, x)

        l, r = l, l

        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        res = []
        for i in range(l + 1, r):
            res.append(arr[i])
        return res

result = Solution().findClosestElements( [1,2,3,4,5], 4, 3)
# result = Solution().findClosestElements( [1,1,2,3,4,5], 4, -1)
print(result)
