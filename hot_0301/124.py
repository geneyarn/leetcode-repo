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

    def maxPath(self, root: TreeNode, cur: int) -> int:
        if not root:
            return 0
        left = max(self.maxPath(root.left, cur + root.val), 0)
        right = max(self.maxPath(root.right, cur + root.val), 0)

        self.ans = max(self.ans, left + right + root.val)

        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root, 0)
        return self.ans
