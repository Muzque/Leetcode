"""

"""
testcases = [
    {
        'input': {
            "target": 12,
            "tree": {
                "nodes": [
                    {"id": "10", "left": "5", "right": "15", "value": 10},
                    {"id": "15", "left": "13", "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": None, "value": 22},
                    {"id": "13", "left": None, "right": "14", "value": 13},
                    {"id": "14", "left": None, "right": None, "value": 14},
                    {"id": "5", "left": "2", "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": None, "value": 2},
                    {"id": "1", "left": None, "right": None, "value": 1}
                ],
                "root": "10"
            }
        },
        'output': 13
    },
]

from lib import gen_tree_root, run_tests


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
def findClosestValueInBst(tree, target):
    ret = None
    diff = float('inf')
    queue = [tree]
    while queue:
        node = queue.pop()
        tmp = abs(target - node.value)
        if tmp < diff:
            diff = tmp
            ret = node.value
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return ret
"""


def search_edges(node, target, closet):
    if node is None:
        return closet
    if abs(node.value - target) < abs(closet - target):
        closet = node.value
    if node.value > target:
        return search_edges(node.left, target, closet)
    if node.value < target:
        return search_edges(node.right, target, closet)
    return closet


def findClosestValueInBst(tree, target):
    return search_edges(tree, target, tree.value)


def main():
    wrapped_cases = []
    for tc in testcases:
        root = gen_tree_root(**tc['input']['tree'])
        wrapped_cases.append({
            'input': {
                'tree': root,
                'target': tc['input']['target']
            },
            'output': tc['output']
        })
    run_tests(
        testcases=wrapped_cases,
        function=findClosestValueInBst,
    )
