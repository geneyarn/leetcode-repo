from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m = len(nums)
        arr = [0] * m
        cur = 0

        for i in range(m):
            v = nums[i]
            l, r = 0, cur
            while l < r:
                mid = (l + r) // 2
                if arr[mid] >= v:
                    r = mid
                else:
                    l = mid + 1
            if l == cur:
                cur += 1
            arr[l] = v
        return cur >= 3


result = Solution().increasingTriplet([1, 2, 3, 4, 5])
print(result)
