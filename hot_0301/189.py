from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m = len(nums)

        tmp = [0] * m
        for i in range(m):
            tmp[(i + k) % m] = nums[i]

        for i in range(m):
            nums[i] = tmp[i]
