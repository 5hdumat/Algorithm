import collections


class Solution:
    def removeDuplicateLettersNonRecur(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)


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

