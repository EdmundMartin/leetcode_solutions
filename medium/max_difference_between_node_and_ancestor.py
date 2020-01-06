"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A
and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recurse_tree(node: TreeNode, min_val: int, max_val: int) -> int:
    if not node:
        return 0

    current_value = max(abs(node.val - min_val), abs(node.val - max_val))
    min_val = min(min_val, node.val)
    max_val = max(max_val, node.val)
    left = recurse_tree(node.left, min_val, max_val)
    right = recurse_tree(node.right, min_val, max_val)

    return max(current_value, left, right)


# Runtime: 40 ms, faster than 51.44% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 17.7 MB, less than 88.89% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return recurse_tree(root, root.val, root.val)
