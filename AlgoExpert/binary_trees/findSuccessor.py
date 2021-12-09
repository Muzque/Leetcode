testcases = [
    {
        'input': {
            "node": "5",
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "parent": None, "right": "3", "value": 1},
                    {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
                    {"id": "3", "left": None, "parent": "1", "right": None, "value": 3},
                    {"id": "4", "left": "6", "parent": "2", "right": None, "value": 4},
                    {"id": "5", "left": None, "parent": "2", "right": None, "value": 5},
                    {"id": "6", "left": None, "parent": "4", "right": None, "value": 6}
                ],
                "root": "1"
            }
        },
        'output': 1,
    },
    {
        'input': {
            "node": "2",
            "tree": {
                "nodes": [
                    {"id": "1", "left": None, "parent": None, "right": "2", "value": 1},
                    {"id": "2", "left": None, "parent": "1", "right": None, "value": 2}
                ],
                "root": "1"
            }
        },
        'output': None,
    },
]

from lib import gen_edges, run_tests


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    def inorder(node, arr):
        if node is None:
            return
        inorder(node.left, arr)
        arr.append(node)
        inorder(node.right, arr)
    arr = []
    inorder(tree, arr)
    arr.append(None)
    for i in range(len(arr)):
        if arr[i] == node:
            return arr[i+1]


if __name__ == '__main__':
    wrapedcases = []
    for tc in testcases:
        edges = gen_edges(tc['input']['tree']['nodes'])
        node_input = edges[int(tc['input']['node']) - 1]
        node_output = edges[tc['output'] - 1] if tc['output'] is not None else tc['output']
        wrapedcases.append({
            'input': {
                'tree': edges[0],
                'node': node_input
            },
            'output': node_output,
        })
    run_tests(
        testcases=wrapedcases,
        function=findSuccessor,
    )
