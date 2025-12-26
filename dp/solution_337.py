# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root in self.memo:
            return self.memo[root]

        rob_it = root.val + (0 if not root.left else self.rob(root.left.left) + self.rob(root.left.right)) + (
            0 if not root.right else self.rob(root.right.left) + self.rob(root.right.right))

        not_rob = self.rob(root.left) + self.rob(root.right)

        res = max(rob_it, not_rob)
        self.memo[root] = res

        return res
