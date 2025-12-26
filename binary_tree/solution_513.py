# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.maxDepth = -1
        self.res = 0

    def traverse(self, root: TreeNode, depth: int):
        if not root:
            return

        if depth > self.maxDepth:
            self.maxDepth = depth
            self.res = root.val

        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 0)
        return self.res


result = Solution().findBottomLeftValue(TreeNode(1, TreeNode(2), TreeNode(3)))
print(result)
