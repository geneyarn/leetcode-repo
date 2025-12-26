# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def __init__(self):
        self.ans = ''

    def traverse(self, root: TreeNode, path: str):
        if not root:
            return

        s = chr(ord('a') + root.val) + path
        if not root.left and not root.right:
            if self.ans > s:
                self.ans = s
            return
        self.traverse(root.left, s)
        self.traverse(root.right, s)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.traverse(root, '')
        return self.ans
