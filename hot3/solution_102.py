# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = [root]

        while q:
            sz = len(q)
            tmp = []
            for i in range(sz):
                n = q.pop(0)
                tmp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ans.append(tmp)
        return ans


result = Solution().levelOrder(TreeNode(3,
                                        TreeNode(9),
                                        TreeNode(20, TreeNode(15, TreeNode(7)))))
print(result)
