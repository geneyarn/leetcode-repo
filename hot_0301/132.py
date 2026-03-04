# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, root: TreeNode, ans: list[int]):
        if not root:
            return
        self.traverse(root.left, ans)
        ans.append(root.val)
        self.traverse(root.right, ans)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse(root)
        return ans
