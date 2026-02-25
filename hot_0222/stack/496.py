from typing import List


class Solution:

    def greater(self, nums: List[int]) -> List[int]:
        m = len(nums)

        ans = [0] * m
        stk = []

        for i in range(m - 1, -1, -1):
            n = nums[i]

            while stk and stk[-1] <= n:
                stk.pop()

            ans[i] = -1 if not stk else stk[-1]
            stk.append(n)
        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.greater(nums2)
        mp = {}

        for i in range(len(greater)):
            mp[nums2[i]] = greater[i]

        return [mp[n] for n in nums1]


result = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
print(result)
