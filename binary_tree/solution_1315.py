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

    def traverse(self, root: TreeNode, parent: TreeNode):
        if not root:
            return

        if parent and parent.val % 2 == 0:
            if root.left:
                self.ans += root.left.val
            if root.right:
                self.ans += root.right.val

        self.traverse(root.left, root)
        self.traverse(root.right, root)

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, None)
        return self.ans


result = Solution().sumEvenGrandparent(TreeNode(6,
                                                TreeNode(7,
                                                         TreeNode(2,
                                                                  TreeNode(9),
                                                                  None),
                                                         TreeNode(7,
                                                                  TreeNode(1),
                                                                  TreeNode(4))),
                                                TreeNode(8,
                                                         TreeNode(1),
                                                         TreeNode(3,
                                                                  None,
                                                                  TreeNode(5)
                                                                  )
                                                         )
                                                )
                                       )

print(result)
