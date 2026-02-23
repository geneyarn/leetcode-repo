# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        l = root.left
        r = root.right

        root.right = l
        root.left = None

        p = root
        while p.right:
            p = p.right
        p.right = r
