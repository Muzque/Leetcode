# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
def traversal(node, array):
    if not array:
        return
    left, right = -1, -1
    for i in range(len(array)):
        if left == -1 and array[i] < node.value:
            left = i
        if right == -1 and array[i] >= node.value:
            right = i
    if left != -1:
        node.left = BST(array[left])
        bound = right if right != -1 else len(array)
        traversal(node.left, array[left + 1:bound])
    if right != -1:
        node.right = BST(array[right])
        traversal(node.right, array[right + 1:len(array)])


def reconstructBst(preOrderTraversalValues):
    n = preOrderTraversalValues.pop(0)
    root = BST(n)
    traversal(root, preOrderTraversalValues)
    return root
"""


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return
    current = preOrderTraversalValues[0]
    pt = len(preOrderTraversalValues)
    for i in range(1, len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= current:
            pt = i
            break
    left = reconstructBst(preOrderTraversalValues[1:pt])
    right = reconstructBst(preOrderTraversalValues[pt:])
    return BST(current, left, right)
