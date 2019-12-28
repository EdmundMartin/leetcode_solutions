"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 52 ms, faster than 99.87% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 23.1 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
