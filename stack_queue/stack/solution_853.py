from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = len(position)

        cars = []
        for i in range(m):
            cars.append([position[i], speed[i]])

        cars.sort(key=lambda x: x[0])

        time = []
        for i in range(m):
            time.append((target - cars[i][0]) / cars[i][1])

        stk = []
        for i in range(m):

            while stk and time[i] >= stk[-1]:
                stk.pop()

            stk.append(time[i])

        return len(stk)


# result = Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
result = Solution().carFleet(10, [0, 4, 2], [2, 1, 3])
print(result)
