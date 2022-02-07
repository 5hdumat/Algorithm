# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def _dfs(node):
            if node is None:
                return 0

            left = _dfs(node.left)
            right = _dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # print(left, right, node.val)
            self.result = max(self.result, left + right)
            return max(left, right)

        _dfs(root)
        return self.result


s = Solution()
s.longestUnivaluePath(TreeNode(5, TreeNode(5, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))))
