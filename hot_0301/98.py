# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def valid(self, root: TreeNode, mi: float, mx: float) -> bool:
        if not root:
            return True
        if root.val <= mi or root.val >= mx:
            return False

        return self.valid(root.left, mi, root.val) and self.valid(root.right, root.val, mx)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, -inf, inf)
