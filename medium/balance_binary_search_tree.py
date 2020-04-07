"""
1382. Balance a Binary Search Tree
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ
by more than 1.

If there is more than one answer, return any of them.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.


Constraints:
The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 380 ms, faster than 36.34% of Python3 online submissions for Balance a Binary Search Tree.
# Memory Usage: 20 MB, less than 100.00% of Python3 online submissions for Balance a Binary Search Tree.
class Solution:

    def balance(self, vals: List[int], left: int, right: int):
        if left <= right:
            middle = (left + right) // 2
            root_node = TreeNode(vals[middle])
            root_node.left = self.balance(vals, left, middle - 1)
            root_node.right = self.balance(vals, middle + 1, right)
            return root_node
        return None

    def balanceBST(self, root: TreeNode) -> TreeNode:
        ordered = []

        def in_order(node: TreeNode):
            if node:
                in_order(node.left)
                ordered.append(node.val)
                in_order(node.right)
        in_order(root)
        return self.balance(ordered, 0, len(ordered) - 1)
