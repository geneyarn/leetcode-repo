# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = (left + right) // 2
        n = TreeNode(nums[mid])
        n.left = self.build(nums, left, mid - 1)
        n.right = self.build(nums, mid + 1, right)

        return n

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)
