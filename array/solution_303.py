from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.tmp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.tmp[i] = self.tmp[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.tmp[right + 1] - self.tmp[left + 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

a = NumArray([-2, 0, 3, -5, 2, -1])
result = a.sumRange(0, 2)
print(result)
result = a.sumRange(2, 5)
print(result)
result = a.sumRange(0, 5)
print(result)
