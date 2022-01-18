# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0

    def isValid_shit(self, s: str) -> bool:
        words = list(s)
        lst = []
        while words:
            p = words.pop()

            if p == '}' or p == ']' or p == ')':
                lst.append(p)
            else:
                if lst and p + lst[-1] in ['{}', '[]', '()']:
                    lst.pop()
                else:
                    return False

        return len(lst) == 0


s = Solution()
print(s.isValid(']'))
# print(s.isValid('()'))
