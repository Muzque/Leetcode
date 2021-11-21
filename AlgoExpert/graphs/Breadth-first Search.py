"""
Sample Input:

        A
   ------------
   B    C     D
 _____       _____
 E   F       G   H
    ____    ____
    I  J       K

Sample output
[A, B, C, D, E, F, G, G, I, J, K]
"""


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = deque([self])
        array.append(self.name)
        while queue:
            node = queue.popleft()
            for child in node.children:
                array.append(child.name)
                queue.append(child)
        return array
