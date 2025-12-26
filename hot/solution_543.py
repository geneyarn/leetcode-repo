# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDiameter(self, root: TreeNode):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if self.res < left + right:
            self.res = left + right

        self.maxDiameter(root.left)
        self.maxDiameter(root.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter(root)
        return self.res
