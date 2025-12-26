from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.nextGreater(nums2)
        mp = {}
        for i in range(len(nums2)):
            mp[nums2[i]] = greater[i]

        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            res[i] = mp[nums1[i]]
        return res

    def nextGreater(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]

            while stk and stk[-1] <= n:
                stk.pop()

            res[i] = -1 if not stk else stk[-1]
            stk.append(n)

        return res


# result = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
result = Solution().nextGreaterElement([3, 1, 5, 7, 9, 2, 6], [1, 2, 3, 5, 6, 7, 9, 11])
print(result)
