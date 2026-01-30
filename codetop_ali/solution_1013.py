from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        target = s // 3
        count = 0
        curSum = 0
        i = 0
        while i < len(arr):
            curSum += arr[i]
            if curSum == target:
                break
            i += 1
        j = i + 1
        while j < len(arr) - 1:
            curSum += arr[j]
            if curSum == 2 * target:
                return True
            j += 1

        return False


# result = Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
# result = Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
# result = Solution().canThreePartsEqualSum([0, 0, 0, 0])
# result = Solution().canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20])
# result = Solution().canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10])
result = Solution().canThreePartsEqualSum([1, -1, 1, -1])
print(result)
