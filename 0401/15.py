class Solution:

    def twoSum(self, nums: list[int], i: int, j: int, target: int) -> list[list[int]]:

        l, r = i, j
        ans = []
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                t1, t2 = nums[l], nums[r]
                ans.append([t1, t2])

                while l < r and nums[l] == t1:
                    l += 1
                while l < r and nums[r] == t2:
                    r -= 1
            else:
                if s < target:
                    l += 1
                else:
                    r -= 1
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        m = len(nums)
        nums.sort()
        ans = []
        for i in range(m):
            n = nums[i]
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            t = self.twoSum(nums, i + 1, m - 1, -n)

            for a in t:
                ans.append([n, a[0], a[1]])

        return ans


# result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
# result = Solution().threeSum([0, 0, 0])
result = Solution().threeSum([0, 0, 0, 0])
print(result)
