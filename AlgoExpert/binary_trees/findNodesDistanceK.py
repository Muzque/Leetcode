"""

"""
testcases = [
    {
        'input': {
            "k": 2,
            "target": 3,
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": None, "right": "6", "value": 3},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "6", "left": "7", "right": "8", "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8}
                ],
                "root": "1"
            }
        },
        'output': [7, 8, 2]
    },
    {
        'input': {
            "k": 6,
            "target": 8,
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": None, "value": 2},
                    {"id": "3", "left": "5", "right": "6", "value": 3},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "6", "left": None, "right": "7", "value": 6},
                    {"id": "7", "left": None, "right": "8", "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8}
                ],
                "root": "1"
            }
        },
        'output': [4],
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
def find_vertices(node, target, arr):
    if node is None:
        return False, -1
    if node.value == target:
        arr.append((node, 0, 0))
        return True, 0
    left_found, left_dist = find_vertices(node.left, target, arr)
    if left_found:
        arr.append((node, -1, left_dist+1))
        return True, left_dist+1
    right_found, right_dist = find_vertices(node.right, target, arr)
    if right_found:
        arr.append((node, 1, right_dist+1))
        return True, right_dist+1
    return False, -1


def find_edges(node, distance, arr):
    if distance < 0 or node is None:
        return
    if distance == 0:
        arr.append(node.value)
        return
    find_edges(node.left, distance-1, arr)
    find_edges(node.right, distance-1, arr)


def findNodesDistanceK(tree, target, k):
    ret = []
    vertices = []
    find_vertices(tree, target, vertices)
    for v in vertices:
        node, direction, distance = v
        diff = k-distance
        if diff < 0:
            continue
        if diff == 0:
            ret.append(node.value)
            continue
        if direction >= 0:
            find_edges(node.left, diff-1, ret)
        if direction <= 0:
            find_edges(node.right, diff-1, ret)
    return ret
"""


def check_vertex(node, distance, arr, direction):
    if distance == 0:
        arr.append(node.value)
    else:
        next_node = node.right if direction else node.left
        find_edges(next_node, distance-1, arr)


def find_vertices(node, target, k, arr):
    if node is None:
        return False, -1
    if node.value == target:
        find_edges(node, k, arr)
        return True, 1
    left_found, left_dist = find_vertices(node.left, target, k, arr)
    if left_found:
        check_vertex(node, k - left_dist, arr, True)
        return True, left_dist+1
    right_found, right_dist = find_vertices(node.right, target, k, arr)
    if right_found:
        check_vertex(node, k - right_dist, arr, False)
        return True, right_dist+1
    return False, -1


def find_edges(node, distance, arr):
    if distance < 0 or node is None:
        return
    if distance == 0:
        arr.append(node.value)
        return
    find_edges(node.left, distance-1, arr)
    find_edges(node.right, distance-1, arr)


def findNodesDistanceK(tree, target, k):
    ret = []
    find_vertices(tree, target, k, ret)
    return ret


if __name__ == '__main__':
    wrapped_cases = []
    for tc in testcases:
        root = gen_tree_root(**tc['input']['tree'])
        wrapped_cases.append({
            'input': {
                'tree': root,
                'target': tc['input']['target'],
                'k': tc['input']['k']
            },
            'output': tc['output']
        })
    run_tests(
        testcases=wrapped_cases,
        function=findNodesDistanceK,
    )
