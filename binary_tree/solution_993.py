# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.parentX = None
        self.parentY = None
        self.depthX = -1
        self.depthY = -1
        self.x = 0
        self.y = 0

    def traverse(self, root: TreeNode, depth: int, parent: TreeNode):
        if not root:
            return

        if root.val == self.x:
            self.parentX = parent
            self.depthX = depth

        if root.val == self.y:
            self.parentY = parent
            self.depthY = depth

        self.traverse(root.left, depth + 1, root)
        self.traverse(root.right, depth + 1, root)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.traverse(root, 0, None)

        if self.depthX == self.depthY and self.parentX != self.parentY:
            return True

        return False
