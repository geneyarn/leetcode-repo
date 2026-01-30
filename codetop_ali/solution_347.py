import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        q = []

        for key in mp.keys():
            heapq.heappush(q, (mp[key], key))

        while len(q) > k:
            heapq.heappop(q)

        res = []
        while q:
            count, key = heapq.heappop(q)
            res.append(key)

        return res


result = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result)
