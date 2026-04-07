# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        ans = 0

        def traverse(n: TreeNode):

            nonlocal idx
            nonlocal ans
            if not n:
                return

            traverse(n.left)
            idx += 1
            if idx == k:
                ans = n.val
                return
            traverse(n.right)

        traverse(root)
        return ans
