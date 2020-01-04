"""
897. Increasing Order Search Tree
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9

Note:
The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 100 ms, faster than 14.01% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Increasing Order Search Tree.
class Solution:

    def dfs_recursive(self, node: TreeNode, results: List):
        if not node:
            return
        self.dfs_recursive(node.left, results)
        results.append(node)
        self.dfs_recursive(node.right, results)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        results = []
        self.dfs_recursive(root, results)

        starter = results[0]
        for idx in range(len(results) - 1):
            current_node = results[idx]
            current_node.right = results[idx + 1]
            current_node.left = None
        final = results[-1]
        final.left = None
        final.right = None
        return starter
