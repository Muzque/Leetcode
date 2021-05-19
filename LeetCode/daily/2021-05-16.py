"""
Binary Tree Cameras
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3745/
"""
"""
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""

testcases = {
    '1': ([[0, 0, None, 0, 0]], 1),
}


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
170 / 170 test cases passed.
Status: Accepted
Runtime: 44 ms
Memory Usage: 14.7 MB
"""


class Solution:

    def _rec(self, node):
        if node is None:
            return 2
        left = self._rec(node.left)
        right = self._rec(node.right)
        if left == 0 or right == 0:
            self.res += 1
            return 1
        return 2 if (left == 1 or right == 1) else 0

    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        root_val = self._rec(root)
        return self.res + (1 if root_val == 0 else 0)
