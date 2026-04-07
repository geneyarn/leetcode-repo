# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(n: TreeNode, mi: float, mx: float) -> bool:
            if not n:
                return True

            if n.val <= mi or n.val >= mx:
                return False

            return valid(n.left, mi, n.val) and valid(n.right, root.val, mx)

        return valid(root, -inf, inf)
