# https://leetcode.com/problems/fibonacci-number/
import collections


class Solution(object):
    # 공간복잡도 O(n) -> O(1)로 줄이기
    def fib_xy(self, n):
        x = 0
        y = 1

        for i in range(n):
            x, y = x + y, x

        return x

    # 상향식(타뷸레이션)
    dp_table = collections.defaultdict(list)

    def fib_table(self, n):
        self.dp_table[0] = 0
        self.dp_table[1] = 1

        for i in range(2, n + 1):
            self.dp_table[i] = self.dp_table[i - 1] + self.dp_table[i - 2]

        return self.dp_table[n]

    # 하향식(메모이제이션)
    dp_memo = collections.defaultdict(list)

    def fib_memo(self, n):
        if n <= 1:
            return n

        # 이미 계산된 값은 dp 배열에서 찾아 바로 반환한다. (메모이제이션인 이유)
        if self.dp_memo[n]:
            return self.dp_memo[n]

        self.dp_memo[n] = self.fib_memo(n - 1) + self.fib_memo(n - 2)

        return self.dp_memo[n]

    # 재귀구조 브루트포스
    def fib_bruteforce(self, n):
        if n <= 1:
            return n

        return self.fib_bruteforce(n - 1) + self.fib_bruteforce(n - 2)


s = Solution()
print(s.fib_memo(5))
print(s.fib_table(5))
print(s.fib_xy(5))
