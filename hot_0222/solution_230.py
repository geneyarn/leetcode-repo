# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.idx = 0
        self.ans = 0

    def traverse(self, root: TreeNode, k: int):
        if not root:
            return
        self.traverse(root.left, k)
        self.idx += 1
        if self.idx == k:
            self.ans = root.val
        self.traverse(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.traverse(root, k)

        return self.ans
