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

    def traverse(self, root: TreeNode):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            self.ans += root.left.val

        self.traverse(root.left)
        self.traverse(root.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.ans
