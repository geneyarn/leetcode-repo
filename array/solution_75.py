from typing import List


class Solution:

    def __init__(self):
        self.tmp = []

    def sortColors(self, nums: List[int]) -> None:
        m = len(nums)
        self.tmp = [0] * m

        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums: list[int], left: int, right: int):
        if left >= right:
            return

        p = self.partition(nums, left, right)
        self.quickSort(nums, left, p - 1)
        self.quickSort(nums, p + 1, right)

    def partition(self, nums: list[int], left: int, right: int) -> int:
        p = nums[left]

        i, j = left + 1, right

        while i <= j:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[j] > p:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]

        return j

    def mergeSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def merge(self, nums: list[int], left: int, mid: int, right: int) -> None:
        for i in range(left, right + 1):
            self.tmp[i] = nums[i]

        i, j = left, mid + 1
        for p in range(left, right + 1):
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == right + 1:
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
