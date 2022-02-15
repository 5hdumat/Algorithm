# https://leetcode.com/problems/implement-trie-prefix-tree/
import collections


class TrieNode():
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            node = node.children[char]

        # 단어가 모두 완성되었음을 구분하기 위한 값
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root

        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]

        else:
            return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]

        else:
            return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_2 = obj.startsWith("apple")
