"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 48 ms, faster than 77.70% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 16.5 MB, less than 100.00% of Python3 online submissions for Balanced Binary Tree.
class Solution:

    def is_balanced(self, node: TreeNode) -> Tuple[bool, int]:
        if not node:
            return True, -1
        left_balanced, left_height = self.is_balanced(node.left)
        right_balanced, right_height = self.is_balanced(node.right)
        node_height = max(left_height, right_height) + 1
        if left_balanced and right_balanced and abs(left_height - right_height) < 2:
            return True, node_height
        return False, node_height

    def isBalanced(self, root: TreeNode) -> bool:
        balanced, _ = self.is_balanced(root)
        return balanced