# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def _dfs(node):
            if node is None:
                return -1

            left = _dfs(node.left)
            right = _dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        _dfs(root)
        return self.longest


s = Solution()
s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)))
