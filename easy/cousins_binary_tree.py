"""
993. Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 28 ms, faster than 81.50% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Cousins in Binary Tree.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_node = None
        y_node = None
        stack = [(root, None, 0)]
        while stack:
            if x_node and y_node:
                break
            node, parent, depth = stack.pop()
            if node.val == x:
                x_node = (parent, depth)
            if node.val == y:
                y_node = (parent, depth)
            if node.left:
                stack.append((node.left, node, depth+1))
            if node.right:
                stack.append((node.right, node, depth+1))
        if x_node[0] == y_node[0]:
            return False
        if x_node[1] != y_node[1]:
            return False
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    s = Solution()
    s.isCousins(root, 3, 4)