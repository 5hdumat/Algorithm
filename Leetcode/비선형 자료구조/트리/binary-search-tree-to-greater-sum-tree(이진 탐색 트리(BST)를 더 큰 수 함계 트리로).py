# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        self.bstToGst(root.right)

        self.sum += root.val
        root.val = self.sum

        self.bstToGst(root.left)

        return root


s = Solution()
s.bstToGst(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
                    TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))))
