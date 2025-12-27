from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = len(arr)
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= (mid + 1) + 5:
                l = mid + 1
            else:
                r = mid - 1

        return l + 1


result = Solution().findKthPositive([2,3,4,7,11], 5)
print(result)
