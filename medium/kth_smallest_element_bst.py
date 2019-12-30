"""
230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 56 ms, faster than 61.24% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 16.6 MB, less than 98.18% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sorted(values, reverse=True)[-k]
