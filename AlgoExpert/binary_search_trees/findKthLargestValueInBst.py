# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traversal(node, array):
    if node is None:
        return
    traversal(node.right, array)
    array.append(node.value)
    traversal(node.left, array)


def findKthLargestValueInBst(tree, k):
    array = []
    traversal(tree, array)
    return array[k - 1]
