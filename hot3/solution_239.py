from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        stk = []
        ans = []
        for i in range(m):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            if stk and i - stk[0] + 1 > k:
                stk.pop(0)

            stk.append(i)
            if i >= k - 1:
                ans.append(nums[stk[0]])
        return ans


# result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
# result = Solution().maxSlidingWindow([1, -1], 1)
# result = Solution().maxSlidingWindow([3, 1, 1, 3], 3)
result = Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)
print(result)
