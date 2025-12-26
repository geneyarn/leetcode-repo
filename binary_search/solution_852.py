from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = left + (right - left) // 2
            if mid + 1 >= len(arr) or arr[mid] >= arr[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


# result = Solution().peakIndexInMountainArray([0, 1, 0])
# result = Solution().peakIndexInMountainArray([0, 2, 1, 0])
result = Solution().peakIndexInMountainArray([0, 10, 5, 2])
print(result)
