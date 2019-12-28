"""
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.


Example 1:
Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]

Output
[null,false,true]

Explanation
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True

Example 2:
Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]

Output
[null,true,true,false]

Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:
Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]

Output
[null,true,false,false,true]

Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True


Constraints:
TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 10^4]
Total calls of find() is between [1, 10^4]
0 <= target <= 10^6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElementsToSlow:

    def __init__(self, root: TreeNode):
        self.root = root
        self.values = []

    def construct_tree(self):
        root = self.root
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            current_val = node.val
            self.values.append(current_val)
            if node.left:
                node.left.val = (2 * current_val) + 1
                stack.append(node.left)
            if node.right:
                node.right.val = (2 * current_val) + 2
                stack.append(node.right)
        return root

    def find(self, target: int) -> bool:
        self.construct_tree()
        return target in self.values


# Runtime: 108 ms, faster than 25.21% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.
# Memory Usage: 17.4 MB, less than 100.00% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root

    def find(self, target: int) -> bool:
        path = []
        node = self.root
        target += 1

        while target != 1:
            if target % 2 == 1:
                path.append('R')
            else:
                path.append('L')
            target //= 2

        while path:
            direction = path.pop()
            if direction == "L":
                if not node.left:
                    return False
                node = node.left
            else:
                if not node.right:
                    return False
                node = node.right

        return len(path) == 0
