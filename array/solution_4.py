from typing import List


class Solution:

    def findMedia(self, nums1: List[int], i1: int, nums2: List[int], i2: int, k: int) -> int:
        len1 = len(nums1) - i1
        len2 = len(nums2) - i2
        if len2 < len1:
            return self.findMedia(nums2, i2, nums1, i1, k)
        if len1 == 0:
            return nums2[i2 + k - 1]
        if k == 1:
            return min(nums2[i2], nums1[i1])

        s1 = i1 + min(k // 2, len1) - 1
        s2 = i2 + min(k // 2, len2) - 1
        if nums1[s1] <= nums2[s2]:
            return self.findMedia(nums1, s1 + 1, nums2, i2, k - (s1 - i1 + 1))
        else:
            return self.findMedia(nums1, i1, nums2, s2 + 1, k - (s2 - i2 + 1))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        left, right = 0, 0
        if totalLen % 2 == 0:
            left = totalLen // 2
            right = left + 1
        else:
            left = (totalLen + 1) // 2
            right = left

        v1 = self.findMedia(nums1, 0, nums2, 0, left)
        v2 = self.findMedia(nums1, 0, nums2, 0, right)

        return (v1 + v2) / 2


result = Solution().findMedianSortedArrays([1, 3], [2])
print(result)
