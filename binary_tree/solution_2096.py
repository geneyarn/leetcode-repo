# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.startValue = 0
        self.destValue = 0
        self.startPath = ''
        self.destPath = ''
        self.path = ''

    def traverse(self, root: TreeNode):
        if root is None:
            return
        if root.val == self.startValue:
            self.startPath = self.path
        elif root.val == self.destValue:
            self.destPath = self.path

            # 二叉树遍历框架
        self.path += 'L'
        self.traverse(root.left)
        self.path = self.path[:-1]

        self.path += 'R'
        self.traverse(root.right)
        self.path = self.path[:-1]

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startValue = startValue
        self.destValue = destValue
        self.traverse(root)

        p = 0

        while p < len(self.startPath) and p < len(self.destPath) and self.startPath[p] == self.destPath[p]:
            p += 1
        self.startPath = self.startPath[p:]
        self.destPath = self.destPath[p:]
        self.startPath = 'U' * len(self.startPath)
        # 组合 startPath 和 destPath 就得到了答案
        return self.startPath + self.destPath


result = Solution().getDirections(TreeNode(5,
                                           TreeNode(1,
                                                    TreeNode(3),
                                                    None),
                                           TreeNode(2, TreeNode(6), TreeNode(4))), 3, 6)
print(result)
