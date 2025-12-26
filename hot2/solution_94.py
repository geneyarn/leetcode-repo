# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = []

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res
