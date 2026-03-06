import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)

        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        q = []
        for c in mp:
            heapq.heappush(q, (mp[c], c))

        while len(q) > k:
            heapq.heappop(q)

        ans = []
        while q:
            c, v = heapq.heappop(q)
            ans.append(v)
        return ans


result = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result)
