# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def traverse(self, root: TreeNode, path: List[str]):
        if not root:
            return

        val = root.val
        path.append(str(val))
        if not root.left and not root.right:
            self.ans.append("->".join(path))

        self.traverse(root.left, path)
        self.traverse(root.right, path)
        path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root, [])
        return self.ans
