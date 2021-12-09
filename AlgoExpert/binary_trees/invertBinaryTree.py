# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    queue = [tree]
    while queue:
        node = queue.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return tree
