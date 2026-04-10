from typing import List


class Solution:

    def __init__(self):
        self.tmp = []

    def sortColors(self, nums: List[int]) -> None:
        m = len(nums)
        # self.tmp = [0] * m
        # self.mergeSort(nums, 0, m - 1)

        self.quickSort(nums, 0, m - 1)

    def quickSort(self, nums: list[int], l: int, r: int):

        if l >= r:
            return

        p = self.partition(nums, l, r)
        self.quickSort(nums, l, p - 1)
        self.quickSort(nums, p + 1, r)

    def partition(self, nums: list[int], l: int, r: int) -> int:
        p = nums[l]

        i, j = l + 1, r

        while i <= j:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[i] > p:
                j -= 1

            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]

        return j

    def mergeSort(self, nums: list[int], l: int, r: int):
        if l >= r:
            return

        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        self.merge(nums, l, mid, r)

    def merge(self, nums: list[int], l: int, mid: int, r: int):
        for i in range(l, r + 1):
            self.tmp[i] = nums[i]

        i, j = l, mid + 1

        for p in range(l, r + 1):
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == r + 1:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] <= self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            else:
                nums[p] = self.tmp[j]
                j += 1


arr = [6, 2, 0, 2, 1, 1, 0, 3, 5]
# arr = [0, 1]
result = Solution().sortColors(arr)
print(arr)
