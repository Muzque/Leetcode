from collections import deque


def find_reporter(node, target):
    if node is None:
        return False
    if target in node.directReports or target is node:
        return True
    found = any([find_reporter(n, target) for n in node.directReports])
    return found


def getLowestCommonManager(topManager, reportOne, reportTwo):
    manager = topManager
    queue = deque([(1, topManager)])
    while queue:
        layer, node = queue.popleft()
        find1 = find_reporter(node, reportOne)
        find2 = find_reporter(node, reportTwo)
        if find1 and find2:
            for n in node.directReports:
                queue.append((layer + 1, n))
            manager = node
    return manager


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
