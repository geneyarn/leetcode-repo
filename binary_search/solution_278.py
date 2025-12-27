# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 0, n
        while i <= j:
            mid = (i + j) // 2
            bad = isBadVersion(mid)
            if bad:
                j = mid - 1
            else:
                i = mid + 1
        return i
