# https://leetcode.com/problems/sum-of-two-integers/

class Solution(object):
    def getSum2(self, a, b):
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > INT_MAX:
            a = ~(a ^ MASK)

        return a

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            Q1 = A & B
            Q2 = A ^ B
            Q3 = carry & Q2
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(sum)

        if carry != 0:
            result.append(1)

        result = int(''.join(list(map(str, result[::-1]))), 2) & MASK

        if result > INT_MAX:
            # 입력값 -12 -13
            # result ^ MASK로 2의 보수 처리를 진행하면 -24가 나온다. 하지만 원하는 값은 -25이므로 ~(NOT)처리를 해준다. (~(NOT)은 2의 보수에서 1을 뺸 값과 같다.)
            result = ~(result ^ MASK)

        return result


# 0011
# 0110
# 0101
s = Solution()
s.getSum2(3, -6)
