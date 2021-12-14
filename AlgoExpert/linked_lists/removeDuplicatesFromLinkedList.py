testcases = [
    {
        'input': {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": "1-2", "value": 1},
                    {"id": "1-2", "next": "1-3", "value": 1},
                    {"id": "1-3", "next": "2", "value": 1},
                    {"id": "2", "next": "3", "value": 3},
                    {"id": "3", "next": "3-2", "value": 4},
                    {"id": "3-2", "next": "3-3", "value": 4},
                    {"id": "3-3", "next": "4", "value": 4},
                    {"id": "4", "next": "5", "value": 5},
                    {"id": "5", "next": "5-2", "value": 6},
                    {"id": "5-2", "next": None, "value": 6}
                ]
            }
        },
        'output': {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "3", "value": 1},
                {"id": "3", "next": "4", "value": 3},
                {"id": "4", "next": "5", "value": 4},
                {"id": "5", "next": "6", "value": 5},
                {"id": "6", "next": None, "value": 6}
            ]
        }
    },
]

from lib import gen_linked_list_head, run_tests


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    tmp = linkedList.next
    while tmp is not None:
        if linkedList.value == tmp.value:
            linkedList.next = tmp.next
            tmp = tmp.next
        else:
            linkedList = tmp
            tmp = linkedList.next
    return head


def main():
    wrapped_cases = []
    key = 'linkedList'
    for tc in testcases:
        head = gen_linked_list_head(**tc['input'][key])
        head_ans = gen_linked_list_head(**tc['output'])
        wrapped_cases.append({
            'input': {
                key: head,
            },
            'output': head_ans,
        })
    run_tests(
        testcases=wrapped_cases,
        function=removeDuplicatesFromLinkedList,
        mode=key,
    )
