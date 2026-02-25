from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = len(position)

        arr = []
        for i in range(m):
            arr.append([position[i], speed[i]])

        arr.sort(key=lambda x: x[0])

        time = []
        for i in range(m):
            time.append((target - arr[i][0]) / arr[i][1])

        stk = []

        for t in time:
            while stk and t >= stk[-1]:
                stk.pop()

            stk.append(t)

        return len(stk)


result = Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
print(result)
