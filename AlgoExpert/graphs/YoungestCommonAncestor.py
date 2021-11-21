

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def get_ancestors(current):
    result = []
    node = current
    while node is not None:
        result.append(node)
        node = node.ancestor
    return result


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestors1 = get_ancestors(descendantOne)
    ancestors2 = get_ancestors(descendantTwo)
    result = None
    step = float('inf')
    for i, a in enumerate(ancestors1):
        for j, b in enumerate(ancestors2):
            if a is b and i + j < step:
                result = a
                step = i + j
    return result

