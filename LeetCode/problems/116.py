"""
116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


# 91ms PR12.34 | 15.8MB PR8.71
class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        queue = deque([root])
        layer = 1
        while queue:
            tmp = None
            for _ in range(layer):
                node = queue.popleft()
                if tmp is None:
                    tmp = node
                else:
                    tmp.next = node
                    tmp = node
                if node.left is not None:
                    queue.extend([node.left, node.right])
            layer *= 2
        return root


# 52ms PR98.09 | 15.6MB PR70.69
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        queue = [root]
        layer = 1
        while queue:
            tmp = None
            for _ in range(layer):
                node = queue.pop(0)
                if tmp is None:
                    tmp = node
                else:
                    tmp.next = node
                    tmp = node
                if node.left is not None:
                    queue.extend([node.left, node.right])
            layer *= 2
        return root
