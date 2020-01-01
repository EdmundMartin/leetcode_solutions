"""
148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from collections import defaultdict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 100 ms, faster than 93.87% of Python3 online submissions for Sort List.
# Memory Usage: 22.1 MB, less than 15.38% of Python3 online submissions for Sort List.
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = defaultdict(list)
        while head:
            nodes[head.val].append(head)
            head = head.next
        sorted_keys = sorted(list(nodes.keys()))
        node_list = []
        for k in sorted_keys:
            vals = nodes[k]
            for val in vals:
                node_list.append(val)
        for i in range(len(node_list)-1):
            n = node_list[i]
            n.next = node_list[i+1]
        node_list[-1].next = None
        return node_list[0]


# Runtime: 88 ms, faster than 98.07% of Python3 online submissions for Sort List.
# Memory Usage: 22 MB, less than 15.38% of Python3 online submissions for Sort List.
class SolutionFaster:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = defaultdict(list)
        while head:
            nodes[head.val].append(head)
            head = head.next
        sorted_keys = sorted(list(nodes.keys()))
        node_list = []
        prev = None
        for k in sorted_keys:
            vals = nodes[k]
            for val in vals:
                node_list.append(val)
                if prev:
                    prev.next = val
                prev = val
        node_list[-1].next = None
        return node_list[0]


# Runtime: 300 ms, faster than 11.18% of Python3 online submissions for Sort List.
# Memory Usage: 39.1 MB, less than 15.38% of Python3 online submissions for Sort List.
class SolutionInPlace:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        middle_node = self.get_middle_node(head)
        middle_next = middle_node.next

        middle_node.next = None

        left_part = self.sortList(head)
        right_part = self.sortList(middle_next)

        return self.merge_sort(left_part, right_part)

    def get_middle_node(self, node: ListNode) -> ListNode:
        if not node:
            return node

        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort(self, left: ListNode, right: ListNode) -> ListNode:
        sorted_node = None
        if not left:
            return right
        if not right:
            return left

        if left.val <= right.val:
            sorted_node = left
            sorted_node.next = self.merge_sort(left.next, right)
        else:
            sorted_node = right
            sorted_node.next = self.merge_sort(left, right.next)
        return sorted_node
