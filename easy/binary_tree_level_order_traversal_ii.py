"""
107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 28 ms, faster than 98.11% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13.1 MB, less than 96.30% of Python3 online submissions for Binary Tree Level Order Traversal II.
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            current_node, lvl = stack.pop()
            levels[lvl].append(current_node.val)
            if current_node.right is not None:
                stack.append((current_node.right, lvl + 1))
            if current_node.left is not None:
                stack.append((current_node.left, lvl + 1))
        results = [0] * len(levels)
        for k, v in levels.items():
            results[k] = v
        return results[::-1]
