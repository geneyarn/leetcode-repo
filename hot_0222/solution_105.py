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

    def build(self, preorder: List[int], pStart: int, pEnd: int, inorder: List[int], inStart: int,
              inEnd: int) -> TreeNode:
        if pStart > pEnd:
            return None
        rootVal = preorder[pStart]
        rootIdx = self.mp[rootVal]
        leftLen = rootIdx - inStart

        n = TreeNode(rootVal)
        n.left = self.build(preorder, pStart + 1, pStart + leftLen, inorder, inStart, rootIdx - 1)
        n.right = self.build(preorder, pStart + leftLen + 1, pEnd, inorder, rootIdx + 1, inEnd)

        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
