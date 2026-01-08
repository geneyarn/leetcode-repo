from typing import List


class Solution:

    def test(self, nums: List[int]):
        arr = [0] * (4 * len(nums))

        def modify(o: int, l: int, r: int, i: int, v: int):
            if l == r:
                arr[o] = v
                return
            m = (l + r) // 2
            if i <= m:
                modify(o * 2, l, m, i, v)
            else:
                modify(o * 2 + 1, m + 1, r, i, v)
            arr[o] = arr[o * 2] + arr[o * 2 + 1]

        def query(o: int, l: int, r: int, L: int, R: int) -> int:
            if L <= l and r <= R:
                return arr[o]
            ans = 0
            m = (l + r) // 2
            if L <= m:
                ans += query(o * 2, l, m, L, R)
            if R > m:
                ans += query(o * 2 + 1, m + 1, r, L, R)
            return ans

        for i, n in enumerate(nums):
            modify(1, 1, len(nums), i + 1, n)

        return query(1, 1, len(nums), 2, 3)


result = Solution().test([1, 2, 3, 4, 5])
print(result)
