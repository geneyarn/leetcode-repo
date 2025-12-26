from typing import List


class Difference:
    def __init__(self, nums: List[int]):
        self.diff = [0] * len(nums)

        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increase(self, i: int, j: int, val: int):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        res[0] = self.diff[0]

        for i in range(1, len(res)):
            res[i] = res[i - 1] + self.diff[i]

        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        d = Difference(nums)

        for i in range(len(bookings)):
            b = bookings[i]
            d.increase(b[0] - 1, b[1] - 1, b[2])

        return d.result()


# result = Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
result = Solution().corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2)
print(result)
