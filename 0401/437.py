# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        mp = {0: 1}

        def traverse(n: TreeNode, cur: int):
            nonlocal ans
            nonlocal mp

            if not n:
                return

            newCur = cur + n.val
            if newCur - targetSum in mp:
                ans += mp[newCur - targetSum]
            mp[newCur] = mp.get(newCur, 0) + 1
            traverse(n.left, newCur)
            traverse(n.right, newCur)

            mp[newCur] = mp[newCur] - 1

        traverse(root, 0)
        return ans


result = Solution().pathSum(TreeNode(1), 0)
print(result)
