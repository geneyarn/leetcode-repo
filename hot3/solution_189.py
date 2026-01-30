from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)

        tmp = [0] * m
        for i in range(m):
            tmp[(i + k) % m] = nums[i]

        for i in range(m):
            nums[i] = tmp[i]


arr = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(arr, 3)
print(arr)
