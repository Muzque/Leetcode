"""
Flatten Binary Tree to Linked List
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3742/
"""

testcases = {
    '1': (
        [
            [1, 2, 5, 3, 4, None, 6]
        ],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    ),
    '2': (
        [
            []
        ], []
    ),
    '3': (
        [
            [0]
        ], [0]
    ),
}


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
right 1 None
right 5 None
right 6 None
right None None
left None None
left None TreeNode{val: 6, left: None, right: None}
left 2 TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}
right 4 TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}
right None TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}
left None TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}
left 3 TreeNode{val: 4, left: None, right: TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}}
right None TreeNode{val: 4, left: None, right: TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}}
left None TreeNode{val: 4, left: None, right: TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}}

"""

"""
225 / 225 test cases passed.
Status: Accepted
Runtime: 40 ms
Memory Usage: 15.2 MB
"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        def rec(node, cut):
            if not node:
                return cut
            cut = rec(node.right, cut)
            cut = rec(node.left, cut)
            node.left = None
            node.right = cut
            return node
        rec(root, None)
