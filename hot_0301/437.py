# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.mp = {0: 1}
        self.ans = 0
        self.target = 0

    def traverse(self, root: TreeNode, cur: int):
        if not root:
            return
        newCur = cur + root.val
        if newCur - self.target in self.mp:
            self.ans += self.mp[newCur - self.target]
        self.mp[newCur] = self.mp.get(newCur, 0) + 1
        self.traverse(root.left, newCur)
        self.traverse(root.right, newCur)
        self.mp[newCur] = self.mp[newCur] - 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target = targetSum

        self.traverse(root, 0)
        return self.ans


result = Solution().pathSum(TreeNode(10,
                                     TreeNode(5,
                                              TreeNode(3,
                                                       TreeNode(3),
                                                       TreeNode(-2)),
                                              TreeNode(2,
                                                       None,
                                                       TreeNode(1))),
                                     TreeNode(-3,
                                              None,
                                              TreeNode(11))), 8)
print(result)
