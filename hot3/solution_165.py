class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")

        idx1, idx2 = 0, 0

        while idx1 < len(arr1) or idx2 < len(arr2):
            n1 = 0
            if idx1 < len(arr1):
                n1 = int(arr1[idx1])
            n2 = 0
            if idx2 < len(arr2):
                n2 = int(arr2[idx2])

            if n1 == n2:
                idx1 += 1
                idx2 += 1
                continue
            if n1 < n2:
                return -1
            else:
                return 1

        return 0


# result = Solution().compareVersion('1.2', '1.10')
result = Solution().compareVersion('1.01', '1.001')
print(result)
