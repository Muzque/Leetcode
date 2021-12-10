"""
            1
        __________
        2        3
    ________   ________
    4      5   6      7

"""
testcases = [
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "4", "left": None, "right": None, "value": 4}
                ],
                "root": "1"
            }
        },
        'output': 18,
    },
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "-1", "value": 1},
                    {"id": "-1", "left": None, "right": None, "value": -1},
                    {"id": "2", "left": None, "right": None, "value": 2}
                ],
                "root": "1"
            }
        },
        'output': 3
    },
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "-5", "right": "3", "value": 1},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "-5", "left": "6", "right": None, "value": -5},
                    {"id": "6", "left": None, "right": None, "value": 6}
                ],
                "root": "1"
            }
        },
        'output': 6
    },
    {
        'input': {
            "tree": {
                "nodes": [
                    {"id": "-2", "left": None, "right": None, "value": -2}
                ],
                "root": "-2"
            }
        },
        'output': -2,
    },
]

from lib import gen_tree_root, run_tests


def find_max_path(node):
    if node is None:
        return 0
    left = find_max_path(node.left)
    right = find_max_path(node.right)
    return max(left, right, 0) + node.value


def maxPathSum(tree):
    queue = [tree]
    ret = float('-inf')
    while queue:
        node = queue.pop()
        left = find_max_path(node.left)
        right = find_max_path(node.right)
        val = max(left + right, left, right) + node.value
        ret = max(ret, val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return ret


if __name__ == '__main__':
    wrapped_cases = []
    for tc in testcases:
        root = gen_tree_root(**tc['input']['tree'])
        wrapped_cases.append({
            'input': {
                'tree': root
            },
            'output': tc['output'],
        })
    run_tests(
        testcases=wrapped_cases,
        function=maxPathSum,
    )
