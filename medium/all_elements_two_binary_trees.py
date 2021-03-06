"""
1305. All Elements in Two Binary Search Trees
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 356 ms, faster than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        all_elements = []
        stack = [root1, root2]
        while stack:
            node = stack.pop()
            if node:
                all_elements.append(node.val)
            if node and node.left:
                stack.append(node.left)
            if node and node.right:
                stack.append(node.right)
        return sorted(all_elements)
