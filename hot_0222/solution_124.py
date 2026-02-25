# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = -inf

    def maxSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = max(self.maxSum(root.left), 0)
        right = max(self.maxSum(root.right), 0)

        mx = root.val + left + right
        self.ans = max(self.ans, mx)

        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum(root)
        return self.ans


# result = Solution().maxPathSum(TreeNode(1,
#                                         TreeNode(2),
#                                         TreeNode(3)))

result = Solution().maxPathSum(TreeNode(-3))
print(result)
