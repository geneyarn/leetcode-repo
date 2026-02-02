from typing import List


class Solution:

    def __init__(self):
        self.tmp = []

    def sortColors(self, nums: List[int]) -> None:
        m = len(nums)
        self.tmp = [0] * m
        self.mergeSort(nums, 0, m - 1)

    def mergeSort(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        self.mergeSort(nums, lo, mid)
        self.mergeSort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums: List[int], lo: int, mid: int, hi: int):
        for i in range(lo, hi + 1):
            self.tmp[i] = nums[i]

        i, j = lo, mid + 1

        for p in range(lo, hi + 1):
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] < self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            else:
                nums[p] = self.tmp[j]
                j += 1


arr = [2, 0, 2, 1, 1, 0, 3]
# arr = [0, 1]
result = Solution().sortColors(arr)
print(arr)
