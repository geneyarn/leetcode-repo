from typing import List


class Solution:

    def find(self, nums1: List[int], l1: int, nums2: List[int], l2: int, k: int) -> int:
        len1 = len(nums1) - l1
        len2 = len(nums2) - l2
        if len2 < len1:
            return self.find(nums2, l2, nums1, l1, k)

        if len1 == 0:
            return nums2[l2 + k - 1]
        if k == 1:
            return min(nums1[l1], nums2[l2])

        n1 = l1 + min(k // 2, len1) - 1
        n2 = l2 + min(k // 2, len2) - 1
        if nums1[n1] < nums2[n2]:
            return self.find(nums1, n1 + 1, nums2, l2, k - (n1 - l1 + 1))
        else:
            return self.find(nums1, l1, nums2, n2 + 1, k - (n2 - l2 + 1))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        # 0, 1, 2, 3
        if total % 2 == 0:
            l = total // 2
            r = l + 1
        else:
            # 0, 1, 2
            l = r = total // 2 + 1

        lValue = self.find(nums1, 0, nums2, 0, l)
        rValue = self.find(nums1, 0, nums2, 0, r)
        return (lValue + rValue) * 0.5


# result = Solution().findMedianSortedArrays([1, 3], [2])
result = Solution().findMedianSortedArrays([1, 3], [2, 4])
print(result)
