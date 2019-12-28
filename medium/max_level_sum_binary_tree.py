"""
1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.


Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2

Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 328 ms, faster than 65.01% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        stack = [(root, 1)]
        level_sum = {}

        top_depth = None
        max_val = float('-inf')

        while stack:
            current_node, depth = stack.pop()
            if depth in level_sum:
                level_sum[depth] += current_node.val
            else:
                level_sum[depth] = current_node.val
            if current_node.left:
                stack.append((current_node.left, depth + 1))
            if current_node.right:
                stack.append((current_node.right, depth + 1))

        for k, v in level_sum.items():
            if v > max_val:
                max_val = v
                top_depth = k
        return top_depth
