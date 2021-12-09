testcases = [
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": None, "right": "6", "value": 3},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": "7", "right": "8", "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8}
                ],
                "root": "1"
            }
        },
        'output': True,
    },
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": None, "right": "6", "value": 3},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": "7", "right": "8", "value": 5},
                    {"id": "6", "left": "9", "right": "10", "value": 6},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "10", "left": None, "right": None, "value": 10},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8}
                ],
                "root": "1"
            }
        },
        'output': False
    },
]

from lib import run_tests, gen_tree_root


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
def find_depth(node, depth=0):
    if node is None:
        return depth
    left = find_depth(node.left, depth+1)
    right = find_depth(node.right, depth+1)
    return max(left, right)


def heightBalancedBinaryTree(tree):
    queue = [tree]
    while queue:
        node = queue.pop()
        left = find_depth(node.left)
        right = find_depth(node.right)
        diff = abs(left - right)
        if diff > 1:
            return False
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return True
"""


def find_depth(node, depth=0):
    if node is None:
        return True, depth
    left_balanced, left = find_depth(node.left, depth+1)
    right_balanced, right = find_depth(node.right, depth+1)
    if not left_balanced or not right_balanced:
        return False, -1
    is_balanced = 1 - abs(left - right) >= 0
    depth = max(left, right)
    return is_balanced, depth


def heightBalancedBinaryTree(tree):
    is_balanced, depth = find_depth(tree)
    return is_balanced


if __name__ == '__main__':
    wrapped_cases = []
    for tc in testcases:
        tree = gen_tree_root(tc['input']['tree']['nodes'])
        wrapped_cases.append({
            'input': {
                'tree': tree,
            },
            'output': tc['output'],
        })
    run_tests(
        testcases=wrapped_cases,
        function=heightBalancedBinaryTree,
    )
