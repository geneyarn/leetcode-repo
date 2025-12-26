from typing import List


class Solution:

    # 搜索左侧边界的二分搜索
    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left

    def leftBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        leftBound = self.left_bound(arr, x)

        left, right = leftBound, leftBound

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        res = []
        for i in range(left + 1, right):
            res.append(arr[i])
        return res


# result = Solution().leftBound([1], 1)
# print(result)

# result = Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5)
# result = Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
# result = Solution().findClosestElements([1], 1, 1)
result = Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1)
print(result)
