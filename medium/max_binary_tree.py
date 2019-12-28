"""
654. Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 180 ms, faster than 94.04% of Python3 online submissions for Maximum Binary Tree.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Maximum Binary Tree.
class Solution:

    def recursive_solution(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        max_idx = nums.index(max(nums))
        root = TreeNode(nums[max_idx])
        root.left = self.recursive_solution(nums[:max_idx])
        root.right = self.recursive_solution(nums[max_idx + 1:])
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.recursive_solution(nums)
