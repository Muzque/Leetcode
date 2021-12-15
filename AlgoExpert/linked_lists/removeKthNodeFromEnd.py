# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    node = head
    counter = 0
    while head is not None:
        if counter > k:
            node = node.next
        head = head.next
        counter += 1
    if counter == k:
        node.value = node.next.value
        node.next = node.next.next
    else:
        node.next = node.next.next
