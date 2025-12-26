# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = []
        q.append(root)

        while q:
            l = len(q)
            res.append(q[-1].val)

            for i in range(l):
                n = q.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return res
