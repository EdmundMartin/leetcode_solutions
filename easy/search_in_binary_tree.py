"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that
the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't
exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format)
as [], not null.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 92 ms, faster than 17.99% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while current_node is not None:
            if val < current_node.val:
                current_node = current_node.left
            elif val > current_node.val:
                current_node = current_node.right
            else:
                return current_node
        return None
