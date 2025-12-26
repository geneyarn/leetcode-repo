# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.traverse(root, 0)
        self.valus = set()

    def traverse(self, root: TreeNode, val: int):
        if not root:
            return

        root.val = val
        self.valus.add(root.val)
        self.traverse(root.left, 2 * val + 1)
        self.traverse(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.valus

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
