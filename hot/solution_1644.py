class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.findP = False
        self.findQ = False

    def find(self, root: TreeNode, pVal: int, qVal: int) -> TreeNode:
        if not root:
            return

        left = self.find(root.left, pVal, qVal)
        right = self.find(root.right, pVal, qVal)

        if left and right:
            return root

        if root.val == pVal:
            self.findP = True
            return root
        if root.val == qVal:
            self.findQ = True
            return root
        return left if left else right

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        n = self.find(root, p.val, q.val)
        if self.findP and self.findQ:
            return n
        return None
