"""
Given a binary search tree (BST) with duplicates, find all the mode(s)
(the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 48 ms, faster than 98.49% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        counts = {}
        stack = [root]
        while stack:
            current_node = stack.pop()
            value = current_node.val
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
        max_val = max(counts.values())
        return [k for k, v in counts.items() if v == max_val]