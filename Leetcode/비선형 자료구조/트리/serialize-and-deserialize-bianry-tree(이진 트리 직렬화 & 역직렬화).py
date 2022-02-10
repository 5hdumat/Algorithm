# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        Q = collections.deque([root])
        res = []

        while Q:
            node = Q.popleft()

            if node:
                Q.append(node.left)
                Q.append(node.right)

                res.append(str(node.val))
            else:
                res.append('#')

        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        if data == '#':
            return []

        nodes = data.split()
        root = TreeNode(nodes[0])
        Q = collections.deque([root])

        child = 1
        while Q:
            node = Q.popleft()

            if nodes[child] is not '#':
                node.left = TreeNode(nodes[child])
                Q.append(node.left)
            child += 1

            if nodes[child] is not '#':
                node.right = TreeNode(nodes[child])
                Q.append(node.right)
            child += 1

        return root

# Your Codec object will be instantiated and called as such:
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
