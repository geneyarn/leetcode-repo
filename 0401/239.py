from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        stk = []
        ans = []
        for i in range(m):
            n = nums[i]

            while stk and nums[stk[-1]] < n:
                stk.pop()

            stk.append(i)
            if stk and i - stk[0] + 1 > k:
                stk.pop(0)

            if i + 1 >= k:
                ans.append(nums[stk[0]])
        return ans


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
