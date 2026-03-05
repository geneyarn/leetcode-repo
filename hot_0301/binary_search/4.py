from typing import List


class Solution:

    def find(self, nums1: list[int], i1, nums2: list[int], i2: int, k: int):
        length1, length2 = len(nums1) - i1, len(nums2) - i2
        if length1 > length2:
            return self.find(nums2, i2, nums1, i1, k)
        if length1 == 0:
            return nums2[i2 + k - 1]
        if k == 1:
            return min(nums1[i1], nums2[i2])

        n1 = i1 + min(length1, k // 2) - 1
        n2 = i2 + min(length2, k // 2) - 1
        if nums1[n1] <= nums2[n2]:
            return self.find(nums1, n1 + 1, nums2, i2, k - (n1 + 1 - i1))
        else:
            return self.find(nums1, i1, nums2, n2 + 1, k - (n2 + 1 - i2))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        all = m + n
        left, right = 0, 0
        if all % 2 == 0:
            left = all // 2
            right = left + 1
        else:
            left = right = all // 2 + 1

        lVal = self.find(nums1, 0, nums2, 0, left)
        rVal = self.find(nums1, 0, nums2, 0, right)
        #
        return (lVal + rVal) * 0.5


result = Solution().findMedianSortedArrays([1], [2, 4])
# result = Solution().findMedianSortedArrays([1, 2], [3, 4])
print(result)
