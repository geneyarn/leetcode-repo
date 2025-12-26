from typing import List


class Solution:

    def daysWithWeight(self, weights: List[int], load: int) -> int:
        res = 0
        i = 0
        while i < len(weights):
            cap = load

            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1

            res += 1
        return res

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            day = self.daysWithWeight(weights, mid)
            if day > days:
                left = mid + 1
            elif day == days:
                right = mid
            else:
                right = mid
        return left


# result = Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
result = Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)
print(result)
