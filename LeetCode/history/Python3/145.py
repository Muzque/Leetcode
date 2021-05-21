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


class Solution1:
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


"""
Runtime: 48 ms, faster than 5.17% of Python3 online submissions
Memory Usage: 14.3 MB, less than 74.26% of Python3 online submissions
"""


class Solution2:
    def _rec(self, node, arr):
        if node is None:
            return
        if node.left:
            arr = self._rec(node.left, arr)
        if node.right:
            arr = self._rec(node.right, arr)
        arr.append(node.val)
        return arr

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self._rec(root, [])


"""
Runtime: 36 ms, faster than 5.17% of Python3 online submissions 
Memory Usage: 14.2 MB, less than 46.01% of Python3 online submissions 
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(
            root.right) + [root.val]
