"""
Binary Tree Level Order Traversal
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/
"""
"""
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
testcases = {
    '1': ([[3, 9, 20, None, None, 15, 7]], [[3], [9, 20], [15, 7]]),
    '2': ([[1]], [[1]]),
    '3': ([[]], []),
    '14': ([[1, 2, 3, 4, None, None, 5]], [[1], [2, 3], [4, 5]]),
}

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
34 / 34 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 14.7 MB
"""


from collections import deque, defaultdict


class Solution:
    def _update(self, node, i):
        if node.left is not None:
            self.cache[i].append(node.left.val)
        if node.right is not None:
            self.cache[i].append(node.right.val)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.cache = defaultdict(list)
        if root is not None:
            self.cache[1].append(root.val)
        queue = deque([(2, root)])
        while queue:
            i, node = queue.popleft()
            if node is not None:
                self._update(node, i)
                if node.left:
                    queue.append((i+1, node.left))
                if node.right:
                    queue.append((i+1, node.right))
        return [arr for arr in self.cache.values()]
