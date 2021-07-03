# https://leetcode.com/problems/most-common-word/

from typing import Counter, List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        
        paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
        
        paragraphs = paragraph.split()
        
        paragraphs = [paragraph for paragraph in paragraphs if paragraph not in banned] 
        
        return Counter(paragraphs).most_common(1)[0][0]

# 코드개선
import collections
from typing import Counter, List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        
        return Counter(counts).most_common(1)[0][0]
        
a = Solution()

a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

# 교재 문제풀이
import collections
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.defaultdict(int)
        
        for word in words:
            counts[word] += 1
            
        return max(counts, key=counts.get)
        
a = Solution()

a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])