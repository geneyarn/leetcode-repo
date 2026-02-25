from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = len(nums)

        stk = []
        ans = [0] * m

        for i in range(2 * m - 1, -1, -1):
            while stk and stk[-1] <= nums[i % m]:
                stk.pop()

            ans[i % m] = -1 if not stk else stk[-1]
            stk.append(nums[i % m])

        return ans
