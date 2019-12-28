"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents
the position (0-indexed) in the linked list where tail connects to. If pos is -1,
then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 44 ms, faster than 95.92% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next

        while slow.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
