from typing import List


class Solution:
    def partition(self, nums: List[int], i: int, j: int) -> int:
        pivot = nums[i]

        left, right = i + 1, j

        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[i], nums[right] = nums[right], nums[i]

        return right

    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = len(nums)
        target = m - k

        i, j = 0, m - 1
        while i <= j:
            p = self.partition(nums, i, j)
            if p == target:
                return nums[p]
            if p < target:
                i = p + 1
            else:
                j = p - 1

        return -1
