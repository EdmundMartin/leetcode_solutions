"""
1008. Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of
node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left,
then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note:
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 36 ms, faster than 77.78% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
class Solution:

    def insert_in_tree(self, node, value):
        if value > node.val:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self.insert_in_tree(node.right, value)
        else:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self.insert_in_tree(node.left, value)

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.insert_in_tree(root, preorder[i])
        return root

