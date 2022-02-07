# https://leetcode.com/problems/maximum-depth-of-binary-tree
import collections
from collections import deque
from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        Q = collections.deque([root])
        depth = 0
        
        while Q:
            depth += 1

            for _ in range(len(Q)):
                node = Q.popleft()

                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)

        print(depth)
        return depth

s = Solution()
s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
