"""
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionToSlow:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_from_a = []
        temp_a = headA
        while temp_a:
            nodes_from_a.append(temp_a)
            temp_a = temp_a.next

        if not nodes_from_a:
            return None

        temp_b = headB
        while temp_b:
            if temp_b in nodes_from_a:
                return temp_b
            temp_b = temp_b.next
        return None


# Runtime: 164 ms, faster than 74.08% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        length_a = 0
        temp_a = headA
        while temp_a:
            length_a += 1
            temp_a = temp_a.next

        length_b = 0
        temp_b = headB
        while temp_b:
            length_b += 1
            temp_b = temp_b.next

        temp_a = headA
        temp_b = headB
        if length_a > length_b:
            nodes_to_skip = length_a - length_b
            for _ in range(nodes_to_skip):
                temp_a = temp_a.next
        elif length_b > length_a:
            nodes_to_skip = length_b - length_a
            for _ in range(nodes_to_skip):
                temp_b = temp_b.next

        while temp_a and temp_b:
            if temp_a == temp_b:
                return temp_a
            temp_a = temp_a.next
            temp_b = temp_b.next

        return None