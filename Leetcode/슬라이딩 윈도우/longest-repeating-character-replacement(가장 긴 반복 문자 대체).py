# https://leetcode.com/problems/longest-repeating-character-replacement/
import collections


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        counter = collections.Counter()
        for right, char in enumerate(s, 1):
            counter[char] += 1
            most = counter.most_common(1)[0][1]

            print(counter)
            print(right, left,most)
            if right - left - most > k:
                counter[s[left]] -= 1
                left += 1

        print(right - left)
        return right - left


s = Solution()
s.characterReplacement("AAABBC", 2)
s.characterReplacement("AABABBA", 1)
s.characterReplacement("ABBAABABBBABBBBABBA", 1)
