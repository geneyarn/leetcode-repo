# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        doIt = (root.val + (0 if not root.left else self.rob(root.left.left) + self.rob(root.left.right)) +
                (0 if not root.right else self.rob(root.right.left) + self.rob(root.right.right)))
        notDo = self.rob(root.left) + self.rob(root.right)

        return max(doIt, notDo)
