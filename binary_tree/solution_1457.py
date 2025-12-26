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
        self.mp = {}

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.mp[root.val] = self.mp.get(root.val, 0) + 1
        if not root.left and not root.right:
            oneCount = 0
            for v in self.mp.values():
                if v % 2 == 1:
                    oneCount += 1
            if oneCount <= 1:
                self.ans += 1
        self.traverse(root.left)
        self.traverse(root.right)
        self.mp[root.val] -= 1

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.ans


result = Solution().pseudoPalindromicPaths(TreeNode(2,
                                                    TreeNode(1,
                                                             TreeNode(1),
                                                             TreeNode(3,
                                                                      None,
                                                                      TreeNode(1))),
                                                    TreeNode(1)))
print(result)
