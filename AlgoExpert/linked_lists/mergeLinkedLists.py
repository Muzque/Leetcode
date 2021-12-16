# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_minor_node(node1, node2):
    if node1 is None:
        return node2, node1, node2.next
    if node2 is None:
        return node1, node1.next, node2
    if node1.value < node2.value:
        return node1, node1.next, node2
    else:
        return node2, node1, node2.next


def mergeLinkedLists(headOne, headTwo):
    head, headOne, headTwo = get_minor_node(headOne, headTwo)
    node = head
    while headOne or headTwo:
        n, headOne, headTwo = get_minor_node(headOne, headTwo)
        node.next = n
        node = n
    return head
