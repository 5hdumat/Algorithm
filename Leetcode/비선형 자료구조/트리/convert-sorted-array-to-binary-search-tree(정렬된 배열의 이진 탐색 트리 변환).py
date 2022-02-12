# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        pivot = len(nums) // 2

        node = TreeNode(nums[pivot])
        node.left = self.sortedArrayToBST(nums[:pivot])
        node.right = self.sortedArrayToBST(nums[pivot + 1:])

        return node


s = Solution()
bst = s.sortedArrayToBST([-10, -7, -6, -3, 0, 5, 6, 7, 9])
