from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionToSlow:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        node_values = []
        while head:
            node_values.append(head.val)
            head = head.next
        result = []
        for idx, value in enumerate(node_values):
            def_val = 0
            for second in range(idx+1, len(node_values)):
                if node_values[second] > value:
                    def_val = node_values[second]
                    break
            result.append(def_val)
        return result


# Runtime: 316 ms, faster than 99.08% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Next Greater Node In Linked List.
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        node_values = []
        while head:
            node_values.append(head.val)
            head = head.next

        result = [0] * len(node_values)
        stack = [0]
        for i, num in enumerate(node_values[1:], 1):
            while stack and node_values[stack[-1]] < num:
                index = stack.pop()
                result[index] = num
            stack.append(i)
        return result
