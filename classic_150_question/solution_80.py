from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)
        i, j = 0, 1

        while j < m:
            if nums[i] == nums[j]:
                if not (i >= 1 and nums[i] == nums[i - 1]):
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

arr = [0,0,1,1,1,1,2,3,3]
result = Solution().removeDuplicates(arr)
print(f"{arr}-----{result}")
