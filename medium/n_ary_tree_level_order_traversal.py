"""
429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""
from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Runtime: 48 ms, faster than 96.28% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for N-ary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]
        levels = defaultdict(list)
        while stack:
            node, lvl = stack.pop()
            levels[lvl].append(node.val)
            for n in node.children[::-1]:
                stack.append((n, lvl + 1))
        result: List[List[int]] = [None] * len(levels)
        for key, value in levels.items():
            result[key] = value
        return result

