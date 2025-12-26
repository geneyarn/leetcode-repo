# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:
            return root

        left = self.find(root.left, val)
        if left:
            return left
        right = self.find(root.right, val)
        if right:
            return right

    def count(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        node = self.find(root, x)

        leftCount = self.count(node.left)
        rightCount = self.count(node.right)
        otherCount = n - 1 - leftCount - rightCount

        return max(leftCount, rightCount, otherCount) > n // 2


result = Solution().btreeGameWinningMove(TreeNode(1, TreeNode(2), TreeNode(3)), 3, )
