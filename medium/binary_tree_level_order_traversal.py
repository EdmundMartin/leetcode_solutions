"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 36 ms, faster than 37.66% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]
        levels = defaultdict(list)
        while stack:
            node, lvl = stack.pop()
            levels[lvl].append(node.val)
            if node.right:
                stack.append((node.right, lvl+1))
            if node.left:
                stack.append((node.left, lvl+1))
        result = []
        for i in range(len(levels)):
            result.append(levels[i])
        return result
