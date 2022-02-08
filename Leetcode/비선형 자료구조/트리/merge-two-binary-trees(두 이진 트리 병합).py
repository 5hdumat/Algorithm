# https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)

            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2


s = Solution()
s.mergeTrees(TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2)),
             TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))))
