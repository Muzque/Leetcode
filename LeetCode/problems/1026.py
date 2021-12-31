"""
1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
testcases = [
    {
        'input': {
            'root': [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13],
        },
        'output': 7,
    }
]

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(node, biggest, smallest, diff):
            if node is None:
                return diff
            biggest = max(biggest, node.val)
            smallest = min(smallest, node.val)
            diff = max(diff, abs(biggest - node.val), abs(smallest - node.val))
            if node.left is not None:
                diff = max(diff, rec(node.left, biggest, smallest, diff))
            if node.right is not None:
                diff = max(diff, rec(node.right, biggest, smallest, diff))
            return diff

        diff = rec(root, root.val, root.val, float('-inf'))
        return diff
