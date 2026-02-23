# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(self, nums: List[int], left: int, right: int) -> TreeNode:
        if right < left:
            return None

        length = right - left + 1
        mid = left + length // 2
        n = TreeNode(nums[mid])
        n.left = self.build(nums, left, mid - 1)
        n.right = self.build(nums, mid + 1, right)

        return n

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        m = len(nums)
        return self.build(nums, 0, m - 1)


result = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print(result)
