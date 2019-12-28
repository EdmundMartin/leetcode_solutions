"""
Given a non-empty binary tree, return the average value of
the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 48 ms, faster than 92.90% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            current_node, level = stack.pop()
            levels[level].append(current_node.val)
            if current_node.right is not None:
                stack.append((current_node.right, level + 1))
            if current_node.left is not None:
                stack.append((current_node.left, level + 1))
        results = [0] * len(levels)
        for k, v in levels.items():
            total = sum(v) / len(v)
            results[k] = total
        return results
