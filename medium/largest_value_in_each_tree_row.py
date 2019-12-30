from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 32 ms, faster than 99.83% of Python3 online submissions for Find Largest Value in Each Tree Row.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Find Largest Value in Each Tree Row.
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        values = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            values[depth].append(node.val)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        res = []
        for _, value in values.items():
            max_level = max(value)
            res.append(max_level)
        return res
