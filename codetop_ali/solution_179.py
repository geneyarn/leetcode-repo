from functools import cmp_to_key
from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        newArr = [str(n) for n in nums]

        def compare(x: str, y: str):
            a, b = x + y, y + x
            if a < b:
                return 1
            elif a > b:
                return -1
            return 0

        newArr.sort(key=cmp_to_key(compare))

        idx = 0
        while idx < len(newArr) and newArr[idx] == '0':
            idx += 1
        if idx == len(newArr):
            return '0'

        return ''.join(newArr[idx:])


# Solution().largestNumber([10, 2])
# result = Solution().largestNumber([3, 30, 34, 5, 9])
result = Solution().largestNumber([0, 0])
print(result)
