# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"

        return root.val + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        l = data.split(",")
        return self._deserialize(l)

    def _deserialize(self, list: List[str]) -> TreeNode:
        if not list:
            return None

        s = list.pop(0)
        if s == '#':
            return None

        n = TreeNode(int(s))
        n.left = self._deserialize(list)
        n.right = self._deserialize(list)

        return n

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
