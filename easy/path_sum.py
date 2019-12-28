"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 40 ms, faster than 89.32% of Python3 online submissions for Path Sum.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Path Sum.
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        target = sum
        stack = [(root, 0)]
        while stack:
            node, current_sum = stack.pop()
            next_sum = current_sum + node.val
            if node.left:
                stack.append((node.left, next_sum))
            if node.right:
                stack.append((node.right, next_sum))
            if not node.left and not node.right:
                current_sum = current_sum + node.val
                if current_sum == target:
                    return True
        return False


if __name__ == '__main__':
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)
    root.left.left.left = TreeNode(7)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    s = Solution()
    result = s.hasPathSum(root, 22)
    print(result)
