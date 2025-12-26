# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def traverse(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(self.traverse(root.left), 0)
        right = max(self.traverse(root.right), 0)

        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.traverse(root)
        return self.ans
