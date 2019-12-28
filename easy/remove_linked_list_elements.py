"""
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 64 ms, faster than 93.91% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current_head = head
        prev = None
        while current_head:
            if current_head.val == val:
                if prev:
                    prev.next = current_head.next
                else:
                    head = current_head.next
                tmp = current_head.next
                current_head.next = None
                current_head = tmp
            else:
                prev = current_head
                current_head = current_head.next
        return head