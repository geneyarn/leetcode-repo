# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        if not root:
            return q

        q.append(root)

        res = []
        res.append(root.val)
        while q:
            tmp = []
            l = len(q)

            for i in range(l):
                n = q.pop(0)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            if tmp:
                res.append(tmp[-1].val)

            q = tmp
        return res


t = TreeNode(1,
             TreeNode(2, None, TreeNode(5)),
             TreeNode(3, None, TreeNode(4)))

result = Solution().rightSideView(t)
