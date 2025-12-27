from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        m = len(arr)
        l, r = 0, m - 1

        while l < r:
            mid = (l + r) //2
            if mid + 1 < m and arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


# result = Solution().peakIndexInMountainArray([0, 1, 0])
# result = Solution().peakIndexInMountainArray([0, 2, 1, 0])
result = Solution().peakIndexInMountainArray([0, 10, 5, 2])
print(result)
