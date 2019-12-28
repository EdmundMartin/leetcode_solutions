"""
Minimum Distance Between BST Nodes
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 28 ms, faster than 96.51% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Distance Between BST Nodes.
class Solution:

    def min_diff_array(self, array):
        array = sorted(array)
        min_diff = float('inf')
        for i in range(1, len(array)):
            diff = abs(array[i] - array[i - 1])
            if diff < min_diff:
                min_diff = diff
        return min_diff

    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        stack = [root]
        while stack:
            current_node = stack.pop()
            values.append(current_node.val)
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
        return self.min_diff_array(values)
