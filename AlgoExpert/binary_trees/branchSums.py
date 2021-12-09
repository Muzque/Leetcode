"""

"""
testcases = [

]


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
def branchSums(root):
    def dfs(node, val, arr):
        if node is None:
            return arr
        val += node.value
        if node.left == node.right is None:
            arr.append(val)
            return arr
        arr = dfs(node.left, val, arr)
        arr = dfs(node.right, val, arr)
        return arr
    arr = dfs(root, 0, [])
    return arr
"""


def branchSums(root):
    def dfs(node, val, arr):
        if node is None:
            return
        val += node.value
        if node.left == node.right is None:
            arr.append(val)
            return
        dfs(node.left, val, arr)
        dfs(node.right, val, arr)
    arr = []
    dfs(root, 0, arr)
    return arr


if __name__ == '__main__':
    for tc in testcases:
        ret = branchSums(tc['input'])
        assert(ret == tc['output'])
