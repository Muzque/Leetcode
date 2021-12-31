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


# 48ms 23.8% | 20.7MB 44.74%
class Solution1:
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


# 44ms 39.3% | 15.2MB 92.42%
class Solution2:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [(root, root.val, root.val)]
        res = 0
        while queue:
            node, big, small = queue.pop(0)
            big = max(node.val, big)
            small = min(node.val, small)
            res = max(res, abs(node.val - big), abs(node.val - small))
            if node.left is not None:
                queue.append((node.left, big, small))
            if node.right is not None:
                queue.append((node.right, big, small))
        return res


# 32ms 94.74% | 21MB 14.26%
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(node, maxm, minm):
            if node is None:
                return 0
            maxm, minm = max(maxm, node.val), min(minm, node.val)
            res = max(abs(node.val - maxm), abs(node.val - minm))
            return max(res, rec(node.left, maxm, minm), rec(node.right, maxm, minm))
        return rec(root, root.val, root.val)
