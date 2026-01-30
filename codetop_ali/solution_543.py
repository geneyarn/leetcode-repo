# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def traverse(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        print(f'{root.val}---{left}---{right}')

        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        return self.ans


result = Solution().diameterOfBinaryTree(TreeNode(1,
                                                  TreeNode(2, TreeNode(4), TreeNode(5)),
                                                  TreeNode(3)))
print(result)
