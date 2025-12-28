from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = len(nums1) - 1
        i, j = m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1
            cur -= 1

        while i >= 0:
            nums1[cur] = nums1[i]
            i -= 1
            cur -= 1
        while j >= 0:
            nums1[cur] = nums2[j]
            j -= 1
            cur -= 1


arr = [1,2,3,0,0,0]
result = Solution().merge(arr, 3, [2,5,6], 3)
print(arr)
