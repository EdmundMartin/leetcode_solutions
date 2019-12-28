"""
108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 64 ms, faster than 93.08% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
class Solution:

    def generate_tree(self, nums):
        if len(nums) == 0:
            return
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        root.left = self.generate_tree(nums[:middle])
        root.right = self.generate_tree(nums[middle+1:])
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.generate_tree(nums)


