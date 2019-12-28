"""

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 44 ms, faster than 60.75% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, [])]
        binary_numbers = []
        while stack:
            current_node, history = stack.pop()
            history = history + [current_node.val]
            if current_node.left is not None:
                stack.append((current_node.left, history))
            if current_node.right is not None:
                stack.append((current_node.right, history))
            if current_node.right is None and current_node.left is None:
                binary_numbers.append(history)
        total = 0
        for hist in binary_numbers:
            total += int(''.join([str(h) for h in hist]), 2)
        return total