"""
1315. Sum of Nodes with Even-Valued Grandparent
Given a binary tree, return the sum of values of nodes with even-valued grandparent.
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 92 ms, faster than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
class Solution:

    def depth_first_search(self, current_node: TreeNode, parent: Optional[TreeNode], grandparent: Optional[TreeNode]):
        if not current_node:
            return
        if grandparent and grandparent.val % 2 == 0:
            self.total += current_node.val
        self.depth_first_search(current_node.left, current_node, parent)
        self.depth_first_search(current_node.right, current_node, parent)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        self.depth_first_search(root, None, None)
        return self.total


# Runtime: 104 ms, faster than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
class SolutionIterative:

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        stack = [(root, None, None)]
        while stack:
            current, parent, grandparent = stack.pop()
            if grandparent and grandparent.val % 2 == 0:
                total += current.val
            if current.left:
                stack.append((current.left, current, parent))
            if current.right:
                stack.append((current.right, current, parent))
        return total
