# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_depth(node, depth=0):
    if node is None:
        return depth
    left = get_depth(node.left, depth + 1)
    right = get_depth(node.right, depth + 1)
    return max(left, right)


def binaryTreeDiameter(tree):
    ret = 0
    queue = [tree]
    while queue:
        node = queue.pop()
        left = get_depth(node.left)
        right = get_depth(node.right)
        ret = max(ret, left + right)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return ret
