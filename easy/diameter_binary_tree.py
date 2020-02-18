"""
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.max_size = 0

        def recurse_tree(node: TreeNode):
            if not node:
                return 0

            left_subtree = recurse_tree(node.left)
            right_subtree = recurse_tree(node.right)

            if (left_subtree + right_subtree) > self.max_size:
                self.max_size = left_subtree + right_subtree

            return 1 + max(left_subtree, right_subtree)

        recurse_tree(root)
        return self.max_size
