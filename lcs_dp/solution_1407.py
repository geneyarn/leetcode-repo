from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)

        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, idx: int, value: int):
            if l == r:
                mx[o] = value
                return
            mid = (l + r) // 2
            if idx <= mid:
                modify(o * 2, l, mid, idx, value)
            else:
                modify(o * 2 + 1, mid + 1, r, idx, value)
            mx[o] = max(mx[2 * o], mx[2 * o + 1])

        def query(o: int, l: int, r: int, L: int, R: int) -> int:
            if L <= l and r <= R:
                return mx[o]
            mid = (l + r) // 2
            ans = 0
            if L <= mid:
                ans = query(o * 2, l, mid, L, R)
            if R > mid:
                ans = max(ans, query(o * 2 + 1, mid + 1, r, L, R))

            return ans

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]
