"""
Middle of Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 28 ms, faster than 94.46% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodes = [head]
        current = head
        count = 1
        while current.next is not None:
            current = current.next
            nodes.append(current)
            count += 1
        result = count // 2
        return nodes[result]
