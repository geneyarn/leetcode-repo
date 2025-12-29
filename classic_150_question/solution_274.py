from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h, i = 0, len(citations) - 1

        while i >= 0 and citations[i] > h:
            i -= 1
            h += 1
        return h
