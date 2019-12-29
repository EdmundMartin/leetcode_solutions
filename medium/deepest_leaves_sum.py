"""
1302. Deepest Leaves Sum
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 92 ms, faster than 100.00% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Deepest Leaves Sum.
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        while True:
            new_stack = []
            total = 0
            while stack:
                node = stack.pop()
                total += node.val
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            if not new_stack:
                break
            stack = new_stack
        return total
