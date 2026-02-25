from typing import List


class Solution:

    def find(self, nums1: List[int], i1: int, nums2: List[int], i2: int, k: int) -> int:
        length1, length2 = len(nums1) - i1, len(nums2) - i2
        if length2 < length1:
            return self.find(nums2, i2, nums1, i1, k)
        if length1 == 0:
            return nums2[i2 + k - 1]
        if k == 1:
            return min(nums1[i1], nums2[i2])

        newIdx1 = i1 + min(length1, k // 2) - 1
        newIdx2 = i2 + min(length2, k // 2) - 1

        if nums1[newIdx1] <= nums2[newIdx2]:
            return self.find(nums1, newIdx1 + 1, nums2, i2, k - (newIdx1 - i1 + 1))
        else:
            return self.find(nums1, i1, nums2, newIdx2 + 1, k - (newIdx2 - i2 + 1))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left, right, total = 0, 0, m + n
        if total % 2 == 0:
            left = total // 2
            right = left + 1
        else:
            left = right = total // 2 + 1

        leftValue = self.find(nums1, 0, nums2, 0, left)
        rightValue = self.find(nums1, 0, nums2, 0, right)

        return (leftValue + rightValue) * 0.5


# 1 2 3 4 5
result = Solution().findMedianSortedArrays([1, 3], [2, 4])
print(result)
