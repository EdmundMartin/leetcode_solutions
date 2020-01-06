
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recurse_tree(node: TreeNode, min_val: int, max_val: int) -> int:
    if not node:
        return 0

    current_value = max(abs(node.val - min_val), abs(node.val - max_val))
    min_val = min(min_val, node.val)
    max_val = max(max_val, node.val)
    left = recurse_tree(node.left, min_val, max_val)
    right = recurse_tree(node.right, min_val, max_val)

    return max(current_value, left, right)


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return recurse_tree(root, root.val, root.val)
