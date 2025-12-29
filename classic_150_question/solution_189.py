from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)

        new = [0] * len(nums)
        for i in range(m):
            new[(i + k) % m] = nums[i]

        for i in range(m):
            nums[i] = new[i]

        print(nums)

arr = [1,2,3,4,5,6,7]
result =Solution().rotate([1,2,3,4,5,6,7], 3)

