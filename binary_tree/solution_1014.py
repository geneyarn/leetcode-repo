import math
from typing import List


class Solution:

    def getRange(self, depth: int):
        start = 2 ** depth
        return [start, start * 2 - 1]

    def pathInZigZagTree(self, label: int) -> List[int]:
        n = label
        path = []
        while n >= 1:
            path.append(n)
            n = n // 2
            if n == 0:
                break

            depth = int(math.log2(n))
            r = self.getRange(depth)
            n = r[1] - (n - r[0])

        path.reverse()
        return path


result = Solution().pathInZigZagTree(14)
print(result)
