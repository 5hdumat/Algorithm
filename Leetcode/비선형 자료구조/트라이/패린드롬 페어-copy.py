# https://leetcode.com/problems/implement-trie-prefix-tree/
import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.word = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    def insert(self, index, word):
        node = self.root

        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_ids.append(index)
            node = node.children[char]

        node.word = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            if node.word != -1:
                if self.is_palindrome(word):
                    result.append([index, node.word])

            if word[0] not in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        if node.word != -1 and index != node.word:
            result.append([index, node.word])

        for i in node.palindrome_ids:
            result.append([index, i])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        results = []
        for index, char in enumerate(words):
            trie.insert(index, char)

        for index, char in enumerate(words):
            results.extend(trie.search(index, char))

        return results

s = Solution()
s.palindromePairs(["cbcb", "abcd", "dcba", "lls", "s", "sssll", "bat", "tab", "cat", "b", "baca"])
