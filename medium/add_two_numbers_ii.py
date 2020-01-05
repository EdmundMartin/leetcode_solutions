"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes
first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_int(list_node: ListNode) -> int:
    head = list_node
    res = ""
    while head:
        res += str(head.val)
        head = head.next
    return int(res)


# Runtime: 76 ms, faster than 26.63% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = list_to_int(l1) + list_to_int(l2)
        as_string = str(result)
        head = ListNode(as_string[0])
        fake_head = head
        for i in range(1, len(as_string)):
            fake_head.next = ListNode(as_string[i])
            fake_head = fake_head.next
        return head
