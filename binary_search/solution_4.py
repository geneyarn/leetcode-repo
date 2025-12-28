from typing import List


class Solution:

    def find(self, nums1: List[int], i1: int, nums2: List[int], i2: int, k: int):
        l1 = len(nums1) - i1
        l2 = len(nums2) - i2
        if l1 > l2:
            return self.find(nums2, i2, nums1, i1, k)
        if l1 == 0:
            return nums2[i2 + k - 1]
        if k == 1:
            return min(nums1[i1], nums2[i2])

        i11 = i1 + min(k // 2, l1) - 1
        i22 = i2 + min(k // 2, l2) - 1
        if nums1[i11] < nums2[i22]:
            return self.find(nums1, i11 + 1, nums2, i2, k - (i11 - i1 + 1))
        else:
            return self.find(nums1, i1, nums2, i22 + 1, k - (i22 - i2 + 1))


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        l, r = 0 , 0
        if total % 2 == 0:
            l = total // 2
            r = l + 1
        else:
            l = r = (total // 2) + 1

        lValue = self.find(nums1, 0, nums2, 0, l)
        rValue = self.find(nums1, 0, nums2, 0, r)

        return (lValue + rValue) * 0.5

# result = Solution().findMedianSortedArrays([1, 3], [2])
result = Solution().findMedianSortedArrays([1, 3], [2, 4])
print(result)
