# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def find(self, root: TreeNode, va1: int, val2: int) -> TreeNode:
        if not root:
            return None

        if root.val == va1 or root.val == val2:
            return root

        left = self.find(root.left, va1, val2)
        right = self.find(root.right, va1, val2)

        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p.val, q.val)
