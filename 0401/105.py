# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.mp = {}

    def build(self, pre: List[int], pLeft: int, pRight: int, inorder: List[int], inLeft: int, inRight: int) -> TreeNode:

        if pLeft > pRight:
            return None

        n = TreeNode(pre[pLeft])
        inIdx = self.mp[pre[pLeft]]
        leftLen = inIdx - inLeft

        n.left = self.build(pre, pLeft + 1, pLeft + leftLen, inorder, inLeft, inIdx - 1)
        n.right = self.build(pre, pLeft + leftLen + 1, pRight, inorder, inIdx + 1, inRight)

        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
