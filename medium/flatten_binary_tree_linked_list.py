"""
114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 36 ms, faster than 87.35% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            if prev is not None:
                prev.right = current_node
                prev.left = None
                prev = current_node
            else:
                prev = current_node