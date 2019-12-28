"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0
or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 24 ms, faster than 88.69% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_str = ""
        next_node = head
        while next_node:
            binary_str += str(next_node.val)
            next_node = next_node.next
        return int(binary_str, 2)