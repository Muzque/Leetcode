from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 48 ms, faster than 5.17% of Python3 online submissions
Memory Usage: 14.2 MB, less than 74.26% of Python3 online submissions
"""


class Solution:
    def _rec(self, node):
        if node is None:
            return
        self._rec(node.left)
        self._rec(node.right)
        self.arr.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.arr = []
        self._rec(root)
        return self.arr
