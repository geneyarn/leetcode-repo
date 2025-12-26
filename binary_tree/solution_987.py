# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.nodes = []

    def traverse(self, root: TreeNode, col: int, row: int):
        if not root:
            return
        self.nodes.append([row, col, root.val])
        self.traverse(root.left, col - 1, row + 1)
        self.traverse(root.right, col + 1, row + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0, 0)

        self.nodes.sort(key=lambda x: (x[1], x[0], x[2]))

        res = []
        preCol = float('-inf')
        for n in self.nodes:
            if preCol != n[1]:
                res.append([])
                preCol = n[1]
            res[-1].append(n[2])

        return res


n = TreeNode(3,
             TreeNode(9),
             TreeNode(20,
                      TreeNode(15),
                      TreeNode(7)))

result = Solution().verticalTraversal(n)
print(result)
