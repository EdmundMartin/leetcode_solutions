"""
83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 40 ms, faster than 87.46% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_head = head
        while current_head:
            current_node = current_head.next
            while current_node and current_node.val == current_head.val:
                current_node = current_node.next
            current_head.next, current_head = current_node, current_head.next
        return head