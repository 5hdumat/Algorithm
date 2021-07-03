# https://leetcode.com/problems/group-anagrams/

import collections
from typing import Collection, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        return list(anagrams.values())
        
a = Solution()

a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])