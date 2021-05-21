from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 40 ms, faster than 5.07% of Python3 online submissions
Memory Usage: 14.2 MB, less than 46.27% of Python3 online submissions
"""


class Solution:
    def _rec(self, node):
        if node is None:
            return
        self._rec(node.left)
        self.arr.append(node.val)
        self._rec(node.right)
        return node

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.arr = []
        self._rec(root)
        return self.arr
