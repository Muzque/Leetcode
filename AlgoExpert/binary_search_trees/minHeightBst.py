class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


from collections import deque


def minHeightBst(array):
    pt = (len(array) - 1) // 2
    root = BST(array[pt])
    queue = deque([(root, array[:pt]), (root, array[pt + 1:])])
    while queue:
        node, arr = queue.popleft()
        if not arr:
            continue
        pt = len(arr) // 2
        node.insert(arr[pt])
        edge = node.left if node.right is None else node.right
        queue.append((edge, arr[:pt]))
        queue.append((edge, arr[pt + 1:]))
    return root
