# https://leetcode.com/problems/group-anagrams/
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for x in strs:
            anagrams[''.join(sorted(x))].append(x)

        return list(anagrams.values())

        # res = []
        # counter = collections.Counter(anagrams)
        # for x in counter.values():
        #     res.append(x)
        #
        # return res


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
