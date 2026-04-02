from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        m = len(nums)
        new = [0] * m

        for i in range(m):
            new[(i + k) % m] = nums[i]

        for i in range(m):
            nums[i] = new[i]
