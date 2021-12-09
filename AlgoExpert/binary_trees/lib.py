from typing import Optional, List
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


def gen_vertices(nodes) -> List[BinaryTree]:
    vertices = []
    for i in range(len(nodes)):
        obj = nodes[i]
        node = BinaryTree(value=obj['value'])
        vertices.append(node)

    for i in range(len(vertices)):
        node = nodes[i]
        edge = vertices[i]
        left = get_index(node['left'])
        right = get_index(node['right'])
        edge.left = None if left is None else vertices[left]
        edge.right = None if right is None else vertices[right]
    return vertices


def gen_tree_root(nodes) -> BinaryTree:
    edges = gen_vertices(nodes)
    return edges[0]


def run_tests(testcases, function):
    for idx, tc in enumerate(testcases, 1):
        print(f'Question {idx}:')
        print(f'Input: {tc["input"]}')
        print(f'Answer: {tc["output"]}')
        ret = function(**tc['input'])
        print(f'Yours: {ret}')
        assert(ret == tc['output'])
        print('-'*87)
