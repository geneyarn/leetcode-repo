# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(self, nums: list[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        idx = (start + end) // 2
        n = TreeNode(nums[idx])
        n.left = self.build(nums, start, idx - 1)
        n.right = self.build(nums, idx + 1, end)

        return n

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)


result = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print(result)
