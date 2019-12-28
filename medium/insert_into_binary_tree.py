"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion. It is
guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains
a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 136 ms, faster than 7.58% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Insert into a Binary Search Tree.
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while True:
            if val < current_node.val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(val)
                    return root
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(val)
                    return root
