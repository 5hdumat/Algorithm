# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            pivot = inorder.index(preorder.pop(0))
            # print(pivot, inorder[pivot])

            node = TreeNode(inorder[pivot])
            node.left = self.buildTree(preorder, inorder[:pivot])
            node.right = self.buildTree(preorder, inorder[pivot + 1:])

            return node


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
