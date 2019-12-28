"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 40 ms, faster than 93.04% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            current_node, depth = stack.pop()
            if current_node.left is not None or current_node.right is not None:
                depth += 1
                max_depth = max(depth, max_depth)
            if current_node.left is not None:
                stack.append((current_node.left, depth))
            if current_node.right is not None:
                stack.append((current_node.right, depth))
        return max_depth
