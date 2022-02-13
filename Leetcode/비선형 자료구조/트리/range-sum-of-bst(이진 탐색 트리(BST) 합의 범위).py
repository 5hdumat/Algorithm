# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node is None:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    def rangeSumBSTStack(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, res = [root], 0

        while stack:
            node = stack.pop()

            if node:
                if node.val > low:
                    stack.append(node.left)

                if node.val < high:
                    stack.append(node.right)

                if low <= node.val <= high:
                    res += node.val

        return res

    def rangeSumBSTQ(self, root: Optional[TreeNode], low: int, high: int) -> int:
        Q, res = collections.deque([root]), 0

        while Q:
            node = Q.popleft()

            if node:
                if node.val > low:
                    Q.append(node.left)

                if node.val < high:
                    Q.append(node.right)

                if low <= node.val <= high:
                    res += node.val

        return res

s = Solution()
s.rangeSumBSTQ(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15)
