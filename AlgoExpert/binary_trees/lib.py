from typing import Optional, List, Dict
"""
Example:
    "nodes": [
        {"id": "1", "left": "2", "parent": None, "right": "3", "value": 1},
        {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
        {"id": "3", "left": None, "parent": "1", "right": None, "value": 3},
        {"id": "4", "left": "6", "parent": "2", "right": None, "value": 4},
        {"id": "5", "left": None, "parent": "2", "right": None, "value": 5},
        {"id": "6", "left": None, "parent": "4", "right": None, "value": 6}
    ]
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_index(index: Optional[str]) -> Optional[int]:
    if index is None:
        return None
    return int(index) - 1


def gen_vertices(nodes) -> Dict[str, BinaryTree]:
    vertices = {}
    for obj in nodes:
        vertices[obj['id']] = BinaryTree(value=obj['value'])

    for obj in nodes:
        node = vertices[obj['id']]
        node.left = vertices[obj['left']] if obj['left'] is not None else None
        node.right = vertices[obj['right']] if obj['right'] is not None else None
    return vertices


def gen_tree_root(nodes, root='1') -> BinaryTree:
    edges = gen_vertices(nodes)
    return edges[root]


def display_test_result(index, case, result):
    is_passed = result == case['output']
    result_string = 'Pass!' if is_passed else 'Fail!'
    print(f'Question {index}:')
    print(f'Test result: {result_string}')
    if not is_passed:
        print(f'Input: {case["input"]}')
        print(f'Answer: {case["output"]}')
        print(f'Yours: {result}')
    print('-' * 87)


def run_tests(testcases, function):
    for idx, tc in enumerate(testcases, 1):
        ret = function(**tc['input'])
        display_test_result(idx, tc, ret)
