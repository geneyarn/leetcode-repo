from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)
        i, j = 0, 1

        while j < m:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i + 1

arr = [1,1,2]
result = Solution().removeDuplicates(arr)
print(f"{arr}-----{result}")
