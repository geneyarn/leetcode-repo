from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = 0
        m = len(gas)
        mi = 1000001
        start = 0

        for i in range(m):
            s += gas[i] - cost[i]
            if s < mi:
                mi = s
                start = i + 1
        if s < 0:
            return -1

        return 0 if start == m else start