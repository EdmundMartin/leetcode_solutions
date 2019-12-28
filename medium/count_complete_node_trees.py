"""
222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        complete = 0
        while stack:
            current_node = stack.pop()
            complete += 1
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
        return complete