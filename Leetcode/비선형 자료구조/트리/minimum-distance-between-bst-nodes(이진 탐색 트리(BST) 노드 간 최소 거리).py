# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return

        self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        self.minDiffInBST(root.right)

        return self.result

    def minDiffInBSTStack(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            pop = stack.pop()

            self.result = min(self.result, pop.val - self.prev)
            self.prev = pop.val

            node = pop.right

        return self.result


s = Solution()
s.minDiffInBSTStack(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))))
