# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List


class Solution(object):
    def compute(self, left, right, op):
        results = []

        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))

        return results

    def diffWaysToCompute(self, expression):
        if expression.isdigit():
            return [expression]

        results = []
        for index, op in enumerate(expression):
            if op in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])

                results.extend(self.compute(left, right, op))

        return results


s = Solution()
# s.diffWaysToCompute("2-1-1")
# s.diffWaysToCompute("2*3-4*5")
s.diffWaysToCompute("11")
