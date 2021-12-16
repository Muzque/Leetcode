# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev = None
    node = head
    while node.next is not None:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    node.next = prev
    return node
