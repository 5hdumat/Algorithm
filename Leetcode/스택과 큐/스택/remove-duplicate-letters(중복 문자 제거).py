# https://leetcode.com/problems/remove-duplicate-letters/

import collections


class Solution:
    def removeDuplicateLettersNonRecur(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for x in s:
            counter[x] -= 1

            if x in seen:
                continue

            if stack and x < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(x)
            seen.add(x)

        print(stack)

    def removeDuplicateLetters(self, s: str) -> str:
        # s: cbacdcbc
        for x in sorted(set(s)):
            suffix = s[s.index(x):]

            if set(suffix) == set(s):
                return x + self.removeDuplicateLetters(suffix.replace(x, ''))

        return ''


s = Solution()
letters = s.removeDuplicateLettersNonRecur("cbacdcbc")
print(letters)
