# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.inMp = {}

    def build(self, pre: List[int], pStart: int, pEnd: int, inorder: List[int], inStart: int, inEnd: int) -> TreeNode:
        if pStart > pEnd:
            return None

        n = TreeNode(pre[pStart])
        inIdx = self.inMp[n.val]
        leftLen = inIdx - inStart

        n.left = self.build(pre, pStart + 1, pStart + leftLen, inorder, inStart, inIdx - 1)
        n.right = self.build(pre, pStart + leftLen + 1, pEnd, inorder, inIdx + 1, inEnd)

        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, v in enumerate(inorder):
            self.inMp[v] = i
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


result = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(result)
