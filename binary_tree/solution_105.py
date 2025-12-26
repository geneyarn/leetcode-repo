# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildNode(self, preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int,
                  inEnd: int) -> TreeNode:
        if preStart > preEnd:
            return None

        rootVal = preorder[preStart]
        inIdx = inorder.index(rootVal)

        leftLen = inIdx - 1 - inStart + 1

        n = TreeNode(rootVal)
        n.left = self.buildNode(preorder, preStart + 1, preStart + 1 + leftLen - 1, inorder, inStart, inIdx - 1)
        n.right = self.buildNode(preorder, preStart + leftLen + 1, preEnd, inorder, inIdx + 1, inEnd)
        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildNode(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


result = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(result)
