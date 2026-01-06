from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj = NumArray([-2, 0, 3, -5, 2, -1])
# print(obj.sumRange(0, 2))
# print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
