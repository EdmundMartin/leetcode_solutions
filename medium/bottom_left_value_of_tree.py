"""
513. Find Bottom Left Tree Value
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 64 ms, faster than 8.13% of Python3 online submissions for Find Bottom Left Tree Value.
# Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Find Bottom Left Tree Value.
class NonOptimalSolution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bottom = (root.val, -1, 0)
        stack = [(root, 0, 0)]
        while stack:
            current_node, depth, is_left = stack.pop()
            if current_node.left is not None:
                stack.append((current_node.left, depth+1, is_left-1))
            if current_node.right is not None:
                stack.append((current_node.right, depth+1, is_left+1))
            b_value, b_depth, _ = bottom
            if depth == b_depth:
                if is_left < bottom[2]:
                    bottom = (current_node.val, depth, is_left)
            if depth > b_depth:
                bottom = (current_node.val, depth, is_left)
        return bottom[0]


# Runtime: 36 ms, faster than 97.26% of Python3 online submissions for Find Bottom Left Tree Value.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Find Bottom Left Tree Value.
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        nodes_by_level = [root]
        result = None

        while root and nodes_by_level:
            next_level_nodes = []
            current_node_values = []

            for node in nodes_by_level:
                current_node_values.append(node.val)

                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            if current_node_values:
                result = current_node_values[0]

            nodes_by_level = next_level_nodes

        return result
