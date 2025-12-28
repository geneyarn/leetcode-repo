import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        target = math.pow(10, 9) + 1

        for n in nums:
            if count == 0:
                target = n
                count = 1
            elif target == n:
                count += 1
            else:
                count -= 1

        return target

result = Solution().majorityElement([2,2,1,1,1,2,2])
print(result)