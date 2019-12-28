"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 32 ms, faster than 89.91% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        uniary_value = root.val
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val != uniary_value:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True