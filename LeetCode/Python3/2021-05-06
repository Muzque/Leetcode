"""
Convert Sorted List to Binary Search Tree
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3733/
"""
"""
32 / 32 test cases passed.
Status: Accepted
Runtime: 128 ms
Memory Usage: 20.5 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def set_node(self, left, right):
        if left > right:
            return
        mid = math.ceil((left+right) / 2)
        return TreeNode(
            val=self.arr[mid],
            left=self.set_node(left,mid-1),
            right=self.set_node(mid+1,right)
        )

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.arr = []
        while head is not None:
            self.arr.append(head.val)
            head = head.next
        root = self.set_node(0, len(self.arr)-1)
        return root
