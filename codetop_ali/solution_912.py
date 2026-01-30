from typing import List


class Solution:

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]

        i, j = left + 1, right

        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]

        return j

    def quickSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        p = self.partition(nums, left, right)
        self.quickSort(nums, left, p - 1)
        self.quickSort(nums, p + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums


# result = Solution().sortArray([5, 2, 3, 1])
result = Solution().sortArray([5, 1, 1, 2, 0, 0])
print(result)
