# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValid(self, root: TreeNode, start: int, end: int) -> bool:
        if not root:
            return True
        if not start < root.val < end:
            return False

        return self.isValid(root.left, start, root.val) and self.isValid(root.right, root.val, end)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
