from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = 0
        m = len(digits)
        i = m - 1
        digits[-1] = digits[-1] + 1

        while i >= 0:
            s = tmp + digits[i]
            digits[i] = s % 10
            tmp = s // 10
            i -= 1

        if tmp > 0:
            return [1] + digits
        return digits


# result = Solution().plusOne([1, 2, 3])
# result = Solution().plusOne([4, 3, 2, 1])
result = Solution().plusOne([9])
print(result)
