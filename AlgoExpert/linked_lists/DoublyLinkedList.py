testcases = [
    {
        'input': {
            "classMethodsToCall": [
                {
                    "arguments": ["5"],
                    "method": "setHead"
                },
                {
                    "arguments": ["4"],
                    "method": "setHead"
                },
                {
                    "arguments": ["3"],
                    "method": "setHead"
                },
                {
                    "arguments": ["2"],
                    "method": "setHead"
                },
                {
                    "arguments": ["1"],
                    "method": "setHead"
                },
                {
                    "arguments": ["4"],
                    "method": "setHead"
                },
                {
                    "arguments": ["6"],
                    "method": "setTail"
                },
                {
                    "arguments": ["6", "3"],
                    "method": "insertBefore"
                },
                {
                    "arguments": ["6", "3-2"],
                    "method": "insertAfter"
                },
                {
                    "arguments": [1, "3-3"],
                    "method": "insertAtPosition"
                },
                {
                    "arguments": [3],
                    "method": "removeNodesWithValue"
                },
                {
                    "arguments": ["2"],
                    "method": "remove"
                },
                {
                    "arguments": [5],
                    "method": "containsNodeWithValue"
                },
                {
                    "arguments": ["6", "2"],
                    "method": "insertAfter",
                },
                {
                    "arguments": [5, "1"],
                    "method": "insertAtPosition"
                },
            ],
            "nodes": [
                {"id": "1", "next": None, "prev": None, "value": 1},
                {"id": "2", "next": None, "prev": None, "value": 2},
                {"id": "3", "next": None, "prev": None, "value": 3},
                {"id": "3-2", "next": None, "prev": None, "value": 3},
                {"id": "3-3", "next": None, "prev": None, "value": 3},
                {"id": "4", "next": None, "prev": None, "value": 4},
                {"id": "5", "next": None, "prev": None, "value": 5},
                {"id": "6", "next": None, "prev": None, "value": 6}
            ]
        },
        'output': [
            {
                "arguments": ["5"],
                "linkedList": {
                    "head": "5",
                    "nodes": [
                        {"id": "5", "next": None, "prev": None, "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["4"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "5", "prev": None, "value": 4},
                        {"id": "5", "next": None, "prev": "4", "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["3"],
                "linkedList": {
                    "head": "3",
                    "nodes": [
                        {"id": "3", "next": "4", "prev": None, "value": 3},
                        {"id": "4", "next": "5", "prev": "3", "value": 4},
                        {"id": "5", "next": None, "prev": "4", "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["2"],
                "linkedList": {
                    "head": "2",
                    "nodes": [
                        {"id": "2", "next": "3", "prev": None, "value": 2},
                        {"id": "3", "next": "4", "prev": "2", "value": 3},
                        {"id": "4", "next": "5", "prev": "3", "value": 4},
                        {"id": "5", "next": None, "prev": "4", "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["1"],
                "linkedList": {
                    "head": "1",
                    "nodes": [
                        {"id": "1", "next": "2", "prev": None, "value": 1},
                        {"id": "2", "next": "3", "prev": "1", "value": 2},
                        {"id": "3", "next": "4", "prev": "2", "value": 3},
                        {"id": "4", "next": "5", "prev": "3", "value": 4},
                        {"id": "5", "next": None, "prev": "4", "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["4"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "3", "prev": "1", "value": 2},
                        {"id": "3", "next": "5", "prev": "2", "value": 3},
                        {"id": "5", "next": None, "prev": "3", "value": 5}
                    ],
                    "tail": "5"
                },
                "method": "setHead",
                "output": None
            },
            {
                "arguments": ["6"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "3", "prev": "1", "value": 2},
                        {"id": "3", "next": "5", "prev": "2", "value": 3},
                        {"id": "5", "next": "6", "prev": "3", "value": 5},
                        {"id": "6", "next": None, "prev": "5", "value": 6}
                    ],
                    "tail": "6"
                },
                "method": "setTail",
                "output": None
            },
            {
                "arguments": ["6", "3"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "5", "prev": "1", "value": 2},
                        {"id": "5", "next": "3", "prev": "2", "value": 5},
                        {"id": "3", "next": "6", "prev": "5", "value": 3},
                        {"id": "6", "next": None, "prev": "3", "value": 6}
                    ],
                    "tail": "6"
                },
                "method": "insertBefore",
                "output": None
            },
            {
                "arguments": ["6", "3-2"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "5", "prev": "1", "value": 2},
                        {"id": "5", "next": "3", "prev": "2", "value": 5},
                        {"id": "3", "next": "6", "prev": "5", "value": 3},
                        {"id": "6", "next": "3-2", "prev": "3", "value": 6},
                        {"id": "3-2", "next": None, "prev": "6", "value": 3}
                    ],
                    "tail": "3-2"
                },
                "method": "insertAfter",
                "output": None
            },
            {
                "arguments": [1, "3-3"],
                "linkedList": {
                    "head": "3",
                    "nodes": [
                        {"id": "3", "next": "4", "prev": None, "value": 3},
                        {"id": "4", "next": "1", "prev": "3", "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "5", "prev": "1", "value": 2},
                        {"id": "5", "next": "3-2", "prev": "2", "value": 5},
                        {"id": "3-2", "next": "6", "prev": "5", "value": 3},
                        {"id": "6", "next": "3-3", "prev": "3-2", "value": 6},
                        {"id": "3-3", "next": None, "prev": "6", "value": 3}
                    ],
                    "tail": "3-3"
                },
                "method": "insertAtPosition",
                "output": None
            },
            {
                "arguments": [3],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "2", "prev": "4", "value": 1},
                        {"id": "2", "next": "5", "prev": "1", "value": 2},
                        {"id": "5", "next": "6", "prev": "2", "value": 5},
                        {"id": "6", "next": None, "prev": "5", "value": 6}
                    ],
                    "tail": "6"
                },
                "method": "removeNodesWithValue",
                "output": None
            },
            {
                "arguments": ["2"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "5", "prev": "4", "value": 1},
                        {"id": "5", "next": "6", "prev": "1", "value": 5},
                        {"id": "6", "next": None, "prev": "5", "value": 6}
                    ],
                    "tail": "6"
                },
                "method": "remove",
                "output": None
            },
            {
                "arguments": [5],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "5", "prev": "4", "value": 1},
                        {"id": "5", "next": "6", "prev": "1", "value": 5},
                        {"id": "6", "next": None, "prev": "5", "value": 6}
                    ],
                    "tail": "6"
                },
                "method": "containsNodeWithValue",
                "output": False
            },
            {
                "arguments": ["6", "2"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "1", "prev": None, "value": 4},
                        {"id": "1", "next": "5", "prev": "4", "value": 1},
                        {"id": "5", "next": "6", "prev": "1", "value": 5},
                        {"id": "6", "next": "2", "prev": "5", "value": 6},
                        {"id": "2", "next": None, "prev": "6", "value": 2},
                    ],
                    "tail": "2"
                },
                "method": "insertAfter",
                "output": False
            },
            {
                "arguments": [5, "1"],
                "linkedList": {
                    "head": "4",
                    "nodes": [
                        {"id": "4", "next": "5", "prev": None, "value": 4},
                        {"id": "5", "next": "6", "prev": "4", "value": 5},
                        {"id": "6", "next": "1", "prev": "5", "value": 6},
                        {"id": "1", "next": "2", "prev": "6", "value": 1},
                        {"id": "2", "next": None, "prev": "1", "value": 2},
                    ],
                    "tail": "2"
                },
                "method": "insertAtPosition",
                "output": True
            },
        ]
    },
]


# This is an input class. Do not edit.
class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.prev = None
        self.next = None

    def __dict__(self):
        return {
            'id': self.id,
            'next': self.next.id if self.next else None,
            'prev': self.prev.id if self.prev else None,
            'value': self.value,
        }


def rename_attr(cached, dc, key):
    if dc[key] is None:
        return dc
    index = dc[key].split('-')[0]
    num = cached.get(index, 0)
    if key == 'next':
        num += 1
    if num <= 1:
        dc[key] = index
    else:
        dc[key] = f'{index}-{num}'
    return dc


def rename_index(cached, dc):
    index = dc['id'].split('-')[0]
    cached[index] = cached.get(index, 0) + 1
    n = cached[index]
    if n == 1:
        dc['id'] = index
    else:
        dc['id'] = f'{index}-{n}'
    return cached, dc


def doublyLinkedList2Dict(klass):
    cached = {}
    ret = {
        'nodes': [],
    }
    node = klass.head
    while node is not None:
        dc = node.__dict__()
        cached, dc = rename_index(cached, dc)
        dc = rename_attr(cached, dc, 'prev')
        dc = rename_attr(cached, dc, 'next')
        ret['nodes'].append(dc)
        node = node.next
    ret['head'] = ret['nodes'][0]['id']
    ret['tail'] = ret['nodes'][-1]['id']
    return ret


def verify_and_display(index, case, klass, ans):
    print(f'Question {index+1}:')
    result = doublyLinkedList2Dict(klass)
    is_passed = result == ans
    result_string = 'Pass!' if is_passed else 'Fail!'
    print(f'Test result: {result_string}')
    if not is_passed:
        print(f'Input: {case}')
        print(f'Answer: {ans}')
        print(f'Yours: {result}')


def get_node(pools, arg):
    if isinstance(arg, str):
        for node in pools:
            if node.id == arg:
                return node
    return arg


def gen_pool(nodes):
    pool = []
    for dc in nodes:
        pool.append(Node(id=dc['id'], value=dc['value']))
    return pool


def main():
    kls = DoublyLinkedList()
    for tc in testcases:
        cases = tc['input']['classMethodsToCall']
        pool = gen_pool(tc['input']['nodes'])
        out = tc['output']
        for idx, cs in enumerate(cases):
            args = [get_node(pool, arg) for arg in cs['arguments']]
            method_name = cs['method']
            getattr(kls, method_name)(*args)
            ans = out[idx]['linkedList']
            verify_and_display(idx, cs, kls, ans)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.chain = []

    def _find_node(self, node):
        for idx in range(len(self.chain)):
            if id(node) == self.chain[idx]:
                return idx
        return -1

    def _pop_node(self, node):
        idx = self._find_node(node)
        if idx == -1:
            return node
        if node.prev is not None:
            node.prev.next = node.next
            if self.tail == node:
                self.tail = node.prev
        if node.next is not None:
            node.next.prev = node.prev
            if self.head == node:
                self.head = node.next
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.prev = None
        node.next = None
        self.chain.pop(idx)
        return node

    def setHead(self, node):
        node = self._pop_node(node)
        if self.tail is None:
            self.tail = node
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self.chain.insert(0, id(node))

    def setTail(self, node):
        node = self._pop_node(node)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.chain.insert(-1, id(node))

    def _insert(self, node, nodeToInsert):
        if node.prev is not None:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
        node.prev = nodeToInsert
        nodeToInsert.next = node
        idx = self._find_node(node)
        self.chain.insert(idx, id(nodeToInsert))
        if self.head == node:
            self.head = nodeToInsert

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert = self._pop_node(nodeToInsert)
        self._insert(node, nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert = self._pop_node(nodeToInsert)
        if node.next is not None:
            node.next.prev = nodeToInsert
            nodeToInsert.next = node.next
        nodeToInsert.prev = node
        node.next = nodeToInsert
        idx = self._find_node(nodeToInsert)
        idx = idx+1 if idx >= 0 else -1
        self.chain.insert(idx, id(nodeToInsert))
        if self.tail is node:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        if position > len(self.chain):
            self.setTail(nodeToInsert)
            return
        node = self.head
        i = 0
        while i < position-1:
            node = node.next
            i += 1
        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            tmp = node
            node = node.next
            if tmp.value == value:
                self._pop_node(tmp)

    def remove(self, node):
        head = self.head
        while head is not None:
            tmp = node
            head = head.next
            if tmp == node:
                self._pop_node(tmp)

    def containsNodeWithValue(self, value):
        head = self.head
        while head is not None:
            if head.value == value:
                return True
            head = head.next
        return False
