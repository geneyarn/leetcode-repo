from typing import List


class Solution:
    def __init__(self):
        self.tmp = []

    def mergeSort(self, nums: List[int], start: int, end: int):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)

        self.merge(nums, start, mid, end)

    def merge(self, nums: List[int], start: int, mid: int, end: int):
        for i in range(start, end + 1):
            self.tmp[i] = nums[i]

        i, j = start, mid + 1
        for p in range(start, end + 1):
            if i >= mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == end + 1:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] <= self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            else:
                nums[p] = self.tmp[j]
                j += 1

    def quickSort(self, nums: List[int], start: int, end: int):
        if start >= end:
            return

        p = self.partition(nums, start, end)
        self.quickSort(nums, start, p - 1)
        self.quickSort(nums, p + 1, end)

    def partition(self, nums: list[int], start: int, end: int) -> int:
        pivot = nums[start]

        i, j = start, end

        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[start] = nums[start], nums[j]

        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = len(nums)
        # self.tmp = [0] * m
        # self.mergeSort(nums, 0, m - 1)

        self.quickSort(nums, 0, m - 1)

        return nums[m - k]


result = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(result)
