# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def collect(self, leaf, name):
        if leaf is None:
            return
        arr = getattr(self, name)
        arr.append(leaf.val)
        if leaf.left is not None and leaf.right is not None:
            self.collect(leaf.left, name)
            self.collect(leaf.right, name)
        elif leaf.left is not None:
            self.collect(leaf.left, name)
            arr.append(None)
        elif leaf.right is not None:
            arr.append(None)
            self.collect(leaf.right, name)

    def isSameTree(self, p, q) -> bool:
        self.arr1 = []
        self.arr2 = []
        self.collect(p, 'arr1')
        self.collect(q, 'arr2')
        return self.arr1 == self.arr2
