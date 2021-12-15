"""

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    tmp = 0
    node1 = linkedListOne
    node2 = linkedListTwo
    while node1 is not None:
        if node2 is not None:
            val = node1.value + node2.value + tmp
        else:
            val = node1.value + tmp
        node1.value = val % 10
        tmp = val // 10
        if node2 is not None:
            node2 = node2.next
        if node1.next is None:
            if node2 is not None or tmp > 0:
                node1.next = LinkedList(0)
        node1 = node1.next
    return linkedListOne
