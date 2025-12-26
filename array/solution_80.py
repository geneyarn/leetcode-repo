from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            else:
                if i <= 0 or nums[i] != nums[i - 1]:
                    i += 1
                    nums[i] = nums[j]
            j += 1
        return i + 1


# result = Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
result = Solution().removeDuplicates([1, 1])
print(result)
