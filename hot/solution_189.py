from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        newArr = [0] * m

        for i in range(m):
            newArr[(i + k) % m] = nums[i]

        for i in range(m):
            nums[i] = newArr[i]


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
