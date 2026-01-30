from typing import List


class Solution:

    def find(self, nums1: List[int], idx1: int, nums2: List[int], idx2: int, k: int):
        length1, length2 = len(nums1) - idx1, len(nums2) - idx2
        if length2 < length1:
            return self.find(nums2, idx2, nums1, idx1, k)
        if length1 == 0:
            return nums2[idx2 + k - 1]
        if k == 1:
            return min(nums1[idx1], nums2[idx2])

        newIdx1 = idx1 + min(length1, k // 2) - 1
        newidx2 = idx2 + min(length2, k // 2) - 1

        if nums1[newIdx1] < nums2[newidx2]:
            return self.find(nums1, newIdx1 + 1, nums2, idx2, k - (newIdx1 - idx1 + 1))
        else:
            return self.find(nums1, idx1, nums2, newidx2 + 1, k - (newidx2 - idx2 + 1))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        left, right = 0, 0
        if (m + n) % 2 == 0:
            left = (m + n) // 2
            right = left + 1
        else:
            left = right = (m + n) // 2 + 1

        leftVal = self.find(nums1, 0, nums2, 0, left)
        rightVal = self.find(nums1, 0, nums2, 0, right)

        return (leftVal + rightVal) * 0.5


result = Solution().findMedianSortedArrays([1, 3], [2])
# result = Solution().findMedianSortedArrays([1, 2], [3, 4])
print(result)
