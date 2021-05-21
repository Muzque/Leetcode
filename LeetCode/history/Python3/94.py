from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 32 ms, faster than 52.65% of Python3 online submissions 
Memory Usage: 14.1 MB, less than 74.55% of Python3 online submissions
"""


class Solution:
    def _rec(self, node):
        if node is None:
            return
        self._rec(node.left)
        self.arr.append(node.val)
        self._rec(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.arr = []
        self._rec(root)
        return self.arr
