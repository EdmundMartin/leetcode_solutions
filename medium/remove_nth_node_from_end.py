"""
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 32 ms, faster than 80.54% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp_node = head

        while n > 0:
            temp_node = temp_node.next
            n -= 1

        if temp_node is None:
            return head.next

        offset_node = head
        while temp_node.next:
            offset_node = offset_node.next
            temp_node = temp_node.next

        offset_node.next = offset_node.next.next
        return head
