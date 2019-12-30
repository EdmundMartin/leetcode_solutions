"""
653. Two Sum IV - Input is a BST
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that
their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True


Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 468 ms, faster than 5.17% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Two Sum IV - Input is a BST.
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        others = []
        stack = [root]
        while stack:
            node = stack.pop()
            target = k - node.val
            if target in others:
                return True
            others.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
