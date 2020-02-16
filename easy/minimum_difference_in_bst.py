"""
530. Minimum Absolute Difference in BST
Given a binary search tree with non-negative values, find the minimum absolute difference between
values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""
from typing import Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.minimum_difference: Union[float, int] = float('inf')
        self.previous_value = None

        def in_order(node: TreeNode):
            if not node:
                return
            in_order(node.left)
            if self.previous_value is not None:
                current_dif = node.val - self.previous_value
                self.minimum_difference = min(self.minimum_difference, current_dif)
            self.previous_value = node.val
            in_order(node.right)

        in_order(root)
        return self.minimum_difference