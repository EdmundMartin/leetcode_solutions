"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2 is None:
            return l1
        elif l2 and l1 is None:
            return l2
        elif l1 is None and l2 is None:
            return None
        p1 = l1
        p1_prev = None
        p2 = l2
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev is not None:
                    p1_prev.next = p2
                p1_prev = p2
                p2 = p2.next
                p1_prev.next = p1
        if p1 is None:
            p1_prev.next = p2
        return l1 if l1.val < l2.val else l2