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
    printc(f'Test result: {result_string}', 'ok2')
    if not is_passed:
        printc(f'Input: {case["input"]}', 'warning')
        printc(f'Answer: {case["output"]}', 'warning')
        printc(f'Yours: {result}', 'warning')
    return is_passed


def run_mem_profiling(function, inputs):
    printc('> profiling memory usage with the last test case...')
    profile_func = profile(func=function)
    profile_func(**inputs)


def summary(results, time_costs, function, tc_input):
    is_all_passed = all(results)
    level = 'ok' if is_all_passed else 'error'
    printc('Examine Report:', 'header')
    printc(f'> all pass: {is_all_passed}', level)
    printc(f'> failed index: {[i + 1 for i, res in enumerate(results) if res is False]}', level)


def run_tests(testcases, function, mode='default'):
    printc(f'Checker mode: {mode}', 'header')
    results = []
    time_costs = 0
    for idx, tc in enumerate(testcases, 1):
        printc(f'Question {idx}:', 'ok2')
        try:
            ret, dt = timeit(function)(**tc['input'])
            is_passed = display_test_result(tc, ret, mode)
            time_costs += dt
        except Exception as e:
            ret = str(e)
            is_passed = display_test_result(tc, ret, mode)
            printc('!!! Exception raised !!!', 'error')
            logging.error(e, exc_info=True)
        results.append(is_passed)
        print('-' * 87)
    summary(results, time_costs, function, tc['input'])


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
        dt = round((te - ts) * 1000, 4)
        print(f'> cost time: {dt}')
        return result, dt
    return timed


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printc(message, level='ok'):
    cached = {
        'header': Colors.HEADER,
        'ok': Colors.OKBLUE,
        'ok2': Colors.OKCYAN,
        'ok3': Colors.OKGREEN,
        'warning': Colors.WARNING,
        'error': Colors.FAIL
    }
    if level not in cached:
        raise Exception(f'Not available message level: {level}')
    start = cached[level]
    end = Colors.ENDC
    print(f'{start}{message}{end}')
