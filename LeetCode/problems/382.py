"""
382. Linked List Random Node
Medium

Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the integer array nums.
int getRandom() Chooses a node randomly from the list and returns its value.
All the nodes of the list should be equally likely to be choosen.
"""

from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 106ms 38.3% | 17.3MB 85.41%
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.cached = []
        while head is not None:
            self.cached.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.cached[random.randint(0, len(self.cached) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
