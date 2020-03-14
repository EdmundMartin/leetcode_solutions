"""
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 32 ms, faster than 70.15% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if not left and not right:
                continue
            if left and not right:
                return False
            if not left and right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
