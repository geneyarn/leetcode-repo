# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.val = 0
        self.targetDepth = 0

    def traverse(self, root: TreeNode, depth: int):
        if not root:
            return

        if depth == self.targetDepth - 1:
            n = TreeNode(self.val)
            n.left = root.left

            r = TreeNode(self.val)
            r.right = root.right

            root.left = n
            root.right = r

        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.val = val
        self.targetDepth = depth

        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n

        self.traverse(root, 1)

        return root
