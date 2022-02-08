# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _bfs(node):
            root = TreeNode()
            root.next = node
            Q = collections.deque([root.next])

            while Q:
                node = Q.popleft()

                if node.left or node.right:
                    node.left, node.right = node.right, node.left

                    Q.append(node.left)
                    Q.append(node.right)

            return root.next

        def _dfs(node):
            root = TreeNode()
            root.next = node
            stack = collections.deque([root.next])

            while stack:
                node = stack.pop()

                if node.left or node.right:
                    node.left, node.right = node.right, node.left

                    stack.append(node.left)
                    stack.append(node.right)

            return root.next

        # def _dfs_my(node):
        #     if node is None:
        #         return None
        #
        #     node_left = _dfs_my(node.left)
        #     node_right = _dfs_my(node.right)
        #
        #     if node_left or node_right:
        #         node.left, node.right = node_right, node_left
        #
        #     return node
        #
        _dfs(root)
        return root


s = Solution()
s.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))
