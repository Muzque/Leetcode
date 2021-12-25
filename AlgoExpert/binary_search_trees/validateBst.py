# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
def validateBst(tree):
    queue = [(tree, float('-inf'), float('inf'))]
    while queue:
        node, left, right = queue.pop()
        if node.right is not None:
            if right > node.right.value >= node.value:
                queue.append((node.right, node.value, right))
            else:
                return False
        if node.left is not None:
            if node.value > node.left.value >= left:
                queue.append((node.left, left, node.value))
            else:
                return False
    return True
"""


def validateBst(tree, left=float('-inf'), right=float('inf')):
    if tree is None:
        return True
    if tree.value >= right or tree.value < left:
        return False
    validateLeft = validateBst(tree.left, left, tree.value)
    validateRight = validateBst(tree.right, tree.value, right)
    return validateLeft and validateRight
