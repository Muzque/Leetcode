sequences = [
    {
        "arguments": [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41],
        "method": "__init__",
        "output": None
    },
    {
        "arguments": [],
        "method": "peek",
        "output": -5
    },
]

from lib import run_sequences


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        idx = (len(array) - 2) // 2
        for i in reversed(range(idx + 1)):
            self.siftDown(i, len(array) - 1, array)
        return array

    def _swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def siftDown(self, start, end, heap):
        left = start * 2 + 1
        while left <= end:
            pt = start * 2 + 2
            right = pt if pt <= end else -1
            idx = right if right != -1 and heap[right] < heap[left] else left
            if heap[idx] < heap[start]:
                self._swap(start, idx, heap)
                start = idx
                left = start * 2 + 1
            else:
                return

    def siftUp(self, idx, heap):
        parent = (idx - 1) // 2
        while idx > 0 and heap[idx] < heap[parent]:
            self._swap(idx, parent, heap)
            idx = parent
            parent = (idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self._swap(0, len(self.heap)-1, self.heap)
        val = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)


def main():
    run_sequences(
        sequences=sequences,
        klass=MinHeap,
    )
