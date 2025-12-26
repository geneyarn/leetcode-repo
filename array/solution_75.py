from typing import List


class Solution:

    def __init__(self):
        self.tmp = []

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.tmp = [0] * len(nums)
        # self.mergeSort(nums, 0, len(nums) - 1)
        self.quickSort(nums, 0, len(nums) - 1)

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
            if i == mid + 1:
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

    def quickSort(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return
        p = self.partition(nums, lo, hi)
        self.quickSort(nums, lo, p - 1)
        self.quickSort(nums, p + 1, hi)

    def partition(self, nums: List[int], lo: int, hi: int) -> int:
        pivot = nums[lo]

        i, j = lo + 1, hi
        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[lo], nums[j] = nums[j], nums[lo]

        return j



# arr = [2, 0, 2, 1, 1, 0, 3]
arr = [0, 1]
result = Solution().sortColors(arr)
print(result)
