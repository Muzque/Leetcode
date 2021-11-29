"""
The height of a binary tree is defined as the length of the longest possible path in the tree.
In particular, a tree consisting of only one node has height 0 and, conventionally, an empty tree has height −1.
For example, the tree shown in the above figure is of height 2.
"""


# Task score 100%
# Correctness 100%
def solution(T):
    def dfs(node, height):
        if node is None:
            return height
        left = dfs(node.l, height+1)
        right = dfs(node.r, height+1)
        return max(left, right)
    height = dfs(T, -1)
    return height
