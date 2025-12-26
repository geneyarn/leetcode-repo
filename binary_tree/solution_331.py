from typing import List


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        list = preorder.split(",")
        return self.serialize(list) and len(list) == 0

    def serialize(self, list: List[str]) -> bool:
        if not list:
            return False

        l = list.pop(0)
        if l == '#':
            return True

        return self.serialize(list) and self.serialize(list)


result = Solution().isValidSerialization("9,#,#,1")
print(result)
