from typing import List


class Solution:

    def __init__(self):
        self.tmp = []

    def partition(self, nums: List[int], l: int, r: int) -> int:
        p = nums[l]

        i, j = l + 1, r
        while i <= j:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[j] > p:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]

        return j

    def findKthLargest2(self, nums: List[int], k: int) -> int:
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

        return 0

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.tmp = [0] * len(nums)

        self.mergeSort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]

    def mergeSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums: List[int], left: int, mid: int, right: int):
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
            elif self.tmp[i] <= self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            else:
                nums[p] = self.tmp[j]
                j += 1


result = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(result)
