# Definition for a binary tree node.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValid(self, root: TreeNode, small: int, big: int) -> bool:
        if not root:
            return True

        return big > root.val > small and self.isValid(root.left, small, root.val) and self.isValid(root.right,
                                                                                                    root.val, big)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -inf, inf)


result = Solution().isValidBST(TreeNode(2,
                                        TreeNode(1),
                                        TreeNode(3)))
print(result)
