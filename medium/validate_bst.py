"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 44 ms, faster than 93.49% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            current_node, min_val, max_val = stack.pop()
            if current_node.val <= min_val or current_node.val >= max_val:
                return False
            if current_node.left:
                stack.append((current_node.left, min_val, current_node.val))
            if current_node.right:
                stack.append((current_node.right, current_node.val, max_val))
        return True


# Runtime: 44 ms, faster than 93.49% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
class SolutionRecursive:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, tree: TreeNode, min_val, max_val) -> bool:
        if not tree:
            return True
        if tree.val <= min_val or tree.val >= max_val:
            return False
        valid_left = self.helper(tree.left, min_val, tree.val)
        valid_right = self.helper(tree.right, tree.val, max_val)
        return valid_left and valid_right
