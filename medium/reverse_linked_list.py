"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 32 ms, faster than 97.17% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1, p2 = None, head
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
