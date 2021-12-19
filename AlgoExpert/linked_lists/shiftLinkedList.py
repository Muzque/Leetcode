# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    tail = head
    length = 1
    while tail.next is not None:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    new_k = length - k if k > 0 else -k
    i = 0
    new_tail = head
    while i < new_k - 1:
        new_tail = new_tail.next
        i += 1
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
