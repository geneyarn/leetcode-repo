from typing import List


class Solution:

    def find(self, nums1: List[int], i1: int, nums2: List[int], i2: int, k: int) -> int:
        m, n = len(nums1), len(nums2)
        len1, len2 = m - i1, n - i2

        if len2 < len1:
            return self.find(nums2, i2, nums1, i1, k)
        if len1 == 0:
            return nums2[i2 + k - 1]
        if k == 1:
            return min(nums1[i1], nums2[i2])

        n1 = i1 + min(len1, k // 2) - 1
        n2 = i2 + min(len2, k // 2) - 1
        if nums1[n1] < nums2[n2]:
            return self.find(nums1, n1 + 1, nums2, i2, k - (n1 + 1 - i1))
        else:
            return self.find(nums1, i1, nums2, n2 + 1, k - (n2 + 1 - i2))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        left, right = 0, 0
        if total % 2 == 0:
            left = total // 2
            right = left + 1
        else:
            left = (total // 2) + 1
            right = left

        leftVal = self.find(nums1, 0, nums2, 0, left)
        rightVal = self.find(nums1, 0, nums2, 0, right)

        return (leftVal + rightVal) * 0.5


# result = Solution().findMedianSortedArrays([1, 3], [2])
result = Solution().findMedianSortedArrays([1, 2], [3, 4])
print(result)
