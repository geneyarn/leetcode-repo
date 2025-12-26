# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildNode(self, inorder: List[int], inStart: int, inEnd: int, postorder: List[int], postStart: int,
                  postEnd: int) -> TreeNode:
        if inStart > inEnd:
            return None

        rootVal = postorder[postEnd]
        inIdx = inorder.index(rootVal)

        leftLen = inIdx - 1 - inStart + 1

        n = TreeNode(rootVal)
        n.left = self.buildNode(inorder, inStart, inIdx - 1, postorder, postStart, postStart + leftLen - 1)
        n.right = self.buildNode(inorder, inIdx + 1, inEnd, postorder, postStart + leftLen, postEnd - 1)

        return n

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildNode(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


result = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(result)
