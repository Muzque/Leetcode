# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Runtime: 48 ms, faster than 5.13% of Python3 online submissions 
Memory Usage: 14.1 MB, less than 73.21% of Python3 online submissions
"""


class Solution:
    def _rec(self, node):
        if node is None:
            return
        self.arr.append(node.val)
        self._rec(node.left)
        self._rec(node.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.arr = []
        self._rec(root)
        return self.arr
