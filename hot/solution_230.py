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
        self.idx = 0

    def traverse(self, root: TreeNode, k: int):
        if not root:
            return
        self.traverse(root.left)
        self.idx += 1
        if self.idx == k:
            self.ans = root.val
            return
        self.traverse(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
