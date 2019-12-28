"""
404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 24 ms, faster than 99.11% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum of Left Leaves.
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack: List[Tuple[TreeNode, Optional[TreeNode]]] = [(root, None)]
        total = 0
        while stack:
            current_node, prev = stack.pop()
            if current_node.left is not None:
                stack.append((current_node.left, current_node))
            if current_node.right is not None:
                stack.append((current_node.right, current_node))

            if current_node.left is None and current_node.right is None:
                if prev and prev.left == current_node:
                    total += current_node.val
        return total