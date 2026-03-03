class Solution:

    def twoSum(self, nums: list[int], i: int, j: int, target: int) -> list[list[[int]]]:
        m = len(nums)

        l, r = i, j
        ans = []
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                ans.append([nums[l], nums[r]])
                n1, n2 = nums[l], nums[r]

                while l < m and nums[l] == n1:
                    l += 1
                while r >= 0 and nums[r] == n2:
                    r -= 1
                continue
            if s < target:
                l += 1
            else:
                r -= 1
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        m = len(nums)

        ans = []
        for i in range(m):
            n = nums[i]
            if i - 1 >= 0 and nums[i - 1] == n:
                continue

            arr = self.twoSum(nums, i + 1, m - 1, -n)
            for a in arr:
                ans.append([n, a[0], a[1]])
        return ans


result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(result)
