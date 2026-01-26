from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        su = sum(nums)

        def check(num: int) -> bool:
            cnt = 1
            s = 0
            for n in nums:
                if s + n <= num:
                    s += n
                    continue
                elif cnt == k:
                    return False

                cnt += 1
                s = n
            return True

        left = ma
        right = su

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# result = Solution().splitArray([7, 2, 5, 10, 8], 2)
result = Solution().splitArray([1, 2, 3, 4, 5], 2)
print(result)
