from typing import List


class QuickSort:

    def partition(self, nums: List[int], lo: int, hi: int) -> int:
        p = nums[0]

        i, j = lo + 1, hi

        while i <= j:
            while i <= hi and nums[i] <= p:
                i += 1

            while j >= lo and nums[j] > p:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]

        return j

    def quickSort(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return

        p = self.partition(nums, lo, hi)
        self.quickSort(nums, lo, p - 1)
        self.quickSort(nums, p + 1, hi)

nums = [5, 1, 2, 3, 4, 8]
QuickSort().quickSort(nums, 0, len(nums) - 1)
print(nums)
