# Definition for a binary tree node.
from functools import cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @cache
    def build(self, l: int, r: int) -> List[TreeNode]:
        res = []
        if l > r:
            res.append(None)
            return res

        for i in range(l, r + 1):
            left = self.build(l, i - 1)
            right = self.build(i + 1, r)

            for n1 in left:
                for n2 in right:
                    n = TreeNode(i)
                    n.left = n1
                    n.right = n2
                    res.append(n)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.build(1, n)
