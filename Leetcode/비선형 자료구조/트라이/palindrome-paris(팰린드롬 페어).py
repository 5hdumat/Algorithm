# https://leetcode.com/problems/palindrome-pairs/
import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.word = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root

        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]

        node.word = index

    def search(self, index: int, word: str) -> List[List[int]]:
        result = []
        node = self.root

        '''
        1) dcbc + d와 같은 조합 판별 (탐색 중간에 word_id가 있고, 나머지 문자가 패린드롬인 경우)

        dcbc(index 3)는 d부터 순차적으로 판별하다가 앞에서 초기화된 d(index 0)의 
        word_id가 -1이 아니면 d를 제외한 cbc가 패린드롬인지를 판별한다. (해당 단어가 패린드롬이라면 정답은 [3, 0]이 된다.)
        '''
        while word:
            if node.word != -1:
                if self.is_palindrome(word):
                    result.append([index, node.word])

            if not word[0] in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        '''
        2) dcbb + bbcd와 같은 조합 판별
        
        단어를 뒤집어서 구축한 트라이 클래스이므로, 찾고자 하는 단어를 순서대로 탐색하다가 끝나는 지점의 word_id가 -1이 아니면 dcbb + bbcd와 같은 조합을 판별할 수 있다.
        '''
        if node.word != -1 and index != node.word:
            result.append([index, node.word])

        '''
        3) bbcd + cbbcd 와 같은 조합 판별
        
        트라이 삽입 중 남아 있는 단어가 패린드롬이라면 palindrome_word_ids에 기록해둔 후, 
        word를 탐색하면서 끝나는 지점의 palindrome_word_ids를 확인 후 값이 존재한다면 정답에 삽입한다.
        '''
        for i in node.palindrome_word_ids:
            result.append([index, i])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        result = []

        for i, v in enumerate(words):
            trie.insert(i, v)

        for index, char in enumerate(words):
            result.extend(trie.search(index, char))

        return result


s = Solution()
s.palindromePairs(["d", "cbbcd", "dcbb", "dcbc", "cbbc", "bbcd"])
