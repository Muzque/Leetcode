"""

"""
testcases = []


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    queue = [(0, root)]
    ret = 0
    while queue:
        depth, node = queue.pop()
        ret += depth
        if node.left is not None:
            queue.append((depth+1, node.left))
        if node.right is not None:
            queue.append((depth+1, node.right))
    return ret
