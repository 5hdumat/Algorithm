# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        if not root:
            return True

        return dfs(root) != -1


root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
# [1,2,2,3,null,null,3,4,null,null,4]
root3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))

s = Solution()
s.isBalanced(root3)
