"""
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 24 ms, faster than 91.51% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        start = dummy
        current = dummy

        for i in range(m):
            start = current
            current = current.next

        tail = current
        prev = None
        for _ in range(n - m + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        start.next = prev
        tail.next = current

        return dummy.next
