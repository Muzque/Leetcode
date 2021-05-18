# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 1st: 20ms, 14MB
    def collect(self, leaf, arr):
        if leaf is None:
            return arr
        arr.append(leaf.val)
        if leaf.left is not None and leaf.right is not None:
            self.collect(leaf.left, arr)
            self.collect(leaf.right, arr)
        elif leaf.left is not None:
            self.collect(leaf.left, arr)
            arr.append(None)
        elif leaf.right is not None:
            arr.append(None)
            self.collect(leaf.right, arr)
        return arr

    def isSameTree(self, p, q) -> bool:
        return self.collect(p, []) == self.collect(q, [])


class Solution2:
    # 2nd: 32ms, 14MB
    def isSameTree(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)
        elif p or q:
            return False
        return True
