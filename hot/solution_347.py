import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for n in nums:
            count = mp.get(n, 0)
            mp[n] = count + 1

        q = []
        for key in mp.keys():
            heapq.heappush(q, (mp[key], key))
            if len(q) > k:
                heapq.heappop(q)

        res = []
        while q:
            res.append(heapq.heappop(q)[1])

        return res
