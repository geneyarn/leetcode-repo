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
        self.idx = 0

    def traverse(self, root: TreeNode, voyage: List[int]) -> bool:
        if not root:
            return True

        if root.val != voyage[self.idx]:
            return False

        self.idx += 1
        if root.left and root.left.val != voyage[self.idx]:
            self.ans.append(root.val)
            root.left, root.right = root.right, root.left

        return self.traverse(root.left, voyage) and self.traverse(root.right, voyage)

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        res = self.traverse(root, voyage)
        if res:
            return self.ans
        else:
            return [-1]
