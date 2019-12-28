"""
Trim Binary Tree
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might
need to change the root of the tree, so the result should return the new
root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 52 ms, faster than 84.57% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Trim a Binary Search Tree.
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def trim(node: TreeNode):
            if not node:
                return
            elif node.val < L:
                return trim(node.right)
            elif node.val > R:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node

        return trim(root)
