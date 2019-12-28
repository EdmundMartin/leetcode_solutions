"""
Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes
overlap, then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 80 ms, faster than 93.10% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Merge Two Binary Trees.
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1:
            return t2
        if not t2:
            return t1

        merged_tree = TreeNode(t1.val + t2.val)
        merged_tree.left = self.mergeTrees(t1.left, t2.left)
        merged_tree.right = self.mergeTrees(t1.right, t2.right)

        return merged_tree
