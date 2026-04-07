# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(n: TreeNode) -> int:
            if not n:
                return 0

            nonlocal ans

            left = depth(n.left)
            right = depth(n.right)

            ans = max(ans, left + right)

            return max(left, right) + 1

        depth(root)
        return ans


# result = Solution().diameterOfBinaryTree(TreeNode(1,
#                                                   TreeNode(2,
#                                                            TreeNode(4), TreeNode(5)),
#                                                   TreeNode(3)))
result = Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2)))
print(result)
