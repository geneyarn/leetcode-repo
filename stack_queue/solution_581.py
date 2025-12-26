from typing import List


class Solution:

    def quickSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        p = self.partition(nums, left, right)
        self.quickSort(nums, left, p - 1)
        self.quickSort(nums, p + 1, right)

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

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsCopy = [0] * len(nums)

        for i in range(len(nums)):
            numsCopy[i] = nums[i]

        self.quickSort(numsCopy, 0, len(numsCopy) - 1)

        left = float('-inf')
        for i in range(len(numsCopy)):
            if numsCopy[i] != nums[i]:
                left = i
                break
        right = float('inf')
        for j in range(len(nums) - 1, -1, -1):
            if numsCopy[j] != nums[j]:
                right = j
                break
        if left == float('-inf') or right == float('inf'):
            return 0
        return right - left + 1


# result = Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
result = Solution().findUnsortedSubarray([1, 2, 3, 4])
print(result)
