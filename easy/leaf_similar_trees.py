"""
Leaf-Similar Trees
Consider all the leaves of a binary tree.  From left to right order,
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 32 ms, faster than 93.97% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs_one = self.process_tree(root1)
        leafs_two = self.process_tree(root2)
        return leafs_one == leafs_two

    def process_tree(self, tree) -> List[int]:
        stack = [tree]
        leafs = []
        while stack:
            current_node = stack.pop()
            if not current_node.left and current_node.right:
                leafs.append(current_node.val)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        return leafs
