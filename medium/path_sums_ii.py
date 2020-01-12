"""
113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 36 ms, faster than 96.83% of Python3 online submissions for Path Sum II.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Path Sum II.
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [])]
        path_sums = []
        while stack:
            node, p = stack.pop()
            temp_path = p[:]
            temp_path.append(node.val)
            if node.left:
                stack.append((node.left, temp_path))
            if node.right:
                stack.append((node.right, temp_path))
            if not node.left and not node.right:
                path_sums.append(temp_path)
        result = []
        for s in path_sums:
            if sum(s) == target:
                result.append(s)
        return result
