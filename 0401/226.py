# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invert(self, root: TreeNode):
        if not root:
            return

        self.invert(root.left)
        self.invert(root.right)

        root.left, root.right = root.right, root.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)

        return root
