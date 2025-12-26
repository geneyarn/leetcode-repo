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
        self.mp = {0: 1}
        self.targetSum = 0

    def traverse(self, root: TreeNode, curSum: int):
        if not root:
            return
        newSum = curSum + root.val
        self.ans += self.mp.get(newSum - self.targetSum, 0)
        self.mp[newSum] = self.mp.get(newSum, 0) + 1

        self.traverse(root.left, curSum)
        self.traverse(root.right, curSum)

        self.mp[newSum] = self.mp[newSum] - 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.mp = {0: 1}
        self.traverse(root, 0)
        return self.ans
