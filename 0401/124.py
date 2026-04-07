# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = -inf

    def maxSum(self, root: TreeNode, cur: int) -> int:
        if not root:
            return 0

        l = max(self.maxSum(root.left, cur + root.val), 0)
        r = max(self.maxSum(root.right, cur + root.val), 0)

        self.ans = max(self.ans, l + r + root.val)

        return max(l, r) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum(root, 0)
        return self.ans
