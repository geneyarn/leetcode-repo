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

    def sumNum(self, root: TreeNode, cur: int):
        if not root:
            return

        if not root.left and not root.right:
            self.ans += (cur + root.val)
            return
        self.sumNum(root.left, cur * 10 + root.val)
        self.sumNum(root.right, cur * 10 + root.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumNum(root, 0)
        return self.ans
