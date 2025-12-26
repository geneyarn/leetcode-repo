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

    def traverse(self, root: TreeNode, val: int):
        if not root:
            return

        newVal = val << 1 | root.val
        if not root.left and not root.right:
            self.ans += newVal
            return
        self.traverse(root.left, newVal)
        self.traverse(root.right, newVal)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 0)
        return self.ans
