"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        min_level = float('inf')
        while stack:
            current_node, level = stack.pop()
            if current_node.left is not None:
                stack.append((current_node.left, level +1))
            if current_node.right is not None:
                stack.append((current_node.right, level +1))
            if current_node.left is None and current_node.right is None:
                min_level = min(min_level, level)
        return min_level
