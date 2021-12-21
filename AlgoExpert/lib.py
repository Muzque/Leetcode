import time
import logging
import operator
from memory_profiler import profile, memory_usage
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


def linkedList2array(linked_list):
    array = []
    while linked_list is not None:
        array.append(linked_list.value)
        linked_list = linked_list.next
    return array


def sort_by_layer(a, b, layer: int):
    if layer == 0:
        sorted_a = sorted(a)
        sorted_b = sorted(b)
    elif layer == 1:
        sorted_a = [sorted(arr) for arr in a]
        sorted_a = sorted(sorted_a, key=operator.itemgetter(0))
        sorted_b = [sorted(arr) for arr in b]
        sorted_b = sorted(sorted_b, key=operator.itemgetter(0))
    else:
        raise Exception(f'Sorting layer exceed: {layer}')
    return sorted_a, sorted_b


def check_result(mode: str, a, b):
    if mode == 'default':
        return a == b
    if mode == 'linkedList':
        tmp_a = linkedList2array(a)
        tmp_b = linkedList2array(b)
        return tmp_a == tmp_b
    if mode.startswith('sort'):
        layer = int(mode.lstrip('sort') or '0')
        tmp_a, tmp_b = sort_by_layer(a, b, layer)
        return tmp_a == tmp_b


def display_test_result(case, result, mode: str):
    is_passed = check_result(mode, case['output'], result)
    result_string = 'Pass!' if is_passed else 'Fail!'
    print(f'Test result: {result_string}')
    if not is_passed:
        print(f'Input: {case["input"]}')
        print(f'Answer: {case["output"]}')
        print(f'Yours: {result}')
    return is_passed


def run_mem_profiling(function, inputs):
    print('> profiling memory usage with the last test case...')
    profile_func = profile(func=function)
    profile_func(**inputs)


def run_tests(testcases, function, mode='default'):
    print(f'Checker mode: {mode}')
    results = []
    time_costs = 0
    for idx, tc in enumerate(testcases, 1):
        print(f'Question {idx}:')
        try:
            ret, dt = timeit(function)(**tc['input'])
            is_passed = display_test_result(tc, ret, mode)
            print(f"Time Costs: {dt} ms")
            time_costs += dt
        except Exception as e:
            ret = str(e)
            is_passed = display_test_result(tc, ret, mode)
            print('!!! Exception raised !!!')
            logging.error(e, exc_info=True)
        results.append(is_passed)
        print('-' * 87)
    is_all_passed = all(results)
    print('Examine Report:')
    print(f'> all pass: {is_all_passed}')
    print(f'> failed index: {[i+1 for i, res in enumerate(results) if res is False]}')
    print(f'> total time costs: {time_costs} ms')
    print(f'> avg. time costs: {time_costs // len(results)} ms')
    if is_all_passed:
        run_mem_profiling(function, tc['input'])


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def gen_linked_list(nodes):
    vertices = {}
    for obj in nodes:
        vertices[obj['id']] = LinkedList(value=obj['value'])
    for obj in nodes:
        vertex = vertices[obj['id']]
        if obj['next'] is not None:
            vertex.next = vertices[obj['next']]
    return vertices


def gen_linked_list_head(nodes, head='1', tail=''):
    vertices = gen_linked_list(nodes)
    return vertices[head]


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        dt = round((te - ts) * 1000, 2)
        return result, dt
    return timed
