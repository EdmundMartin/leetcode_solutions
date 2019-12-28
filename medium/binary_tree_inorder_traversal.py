"""
Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        visited = []
        while stack:
            if root.left is not None:
                stack.append(root.left)
                root = root.left
            else:
                head = stack.pop()
                visited.append(head.val)
                if root.right is not None:
                    stack.append(root.right)
                    root = root.right
                else:
                    while stack:
                        head = stack.pop()
                        visited.append(head.val)
                        if head.right is not None:
                            stack.append(head.right)
                            root = head.right
                            break
        return visited


# Runtime: 28 ms, faster than 93.07% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
class SolutionRecursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        self.recurse(root, visited)
        return visited

    def recurse(self, root: TreeNode, visited: List[int]):
        if root is None:
            return
        if root.left is not None:
            self.recurse(root.left, visited)

        visited.append(root.val)

        if root.right is not None:
            self.recurse(root.right, visited)