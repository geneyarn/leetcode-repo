# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def same(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.same(left.left, right.right) and self.same(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.same(root, root)
