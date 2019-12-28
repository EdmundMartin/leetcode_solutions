"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 60 ms, faster than 99.46% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = self.follow_nodes(l1)
        other = self.follow_nodes(l2)
        total = num + other
        return self.build_list_node(total)

    def convert(self, integers: List[int]):
        s = [str(s) for s in integers]
        return int(''.join(s[::-1]))

    def follow_nodes(self, list_node: ListNode) -> int:
        values = []
        current_node = list_node
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return self.convert(values)

    def build_list_node(self, result: int):
        result = str(result)[::-1]
        node = ListNode(int(result[0]))
        current_node = node
        for i, val in enumerate(result):
            if i > 0:
                current_node.next = ListNode(int(val))
                current_node = current_node.next
        return node


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = s.addTwoNumbers(l1, l2)
    print(result)