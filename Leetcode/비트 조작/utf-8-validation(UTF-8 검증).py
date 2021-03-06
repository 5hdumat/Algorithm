# https://leetcode.com/problems/utf-8-validation/

class Solution(object):
    def validUtf8(self, data):
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False

            return True

        start = 0
        while start < len(data):
            first = data[start]
            if first >> 3 == 0b11110 and check(3):
                start += 4
            elif first >> 4 == 0b1110 and check(2):
                start += 3
            elif first >> 5 == 0b110 and check(1):
                start += 2
            elif first >> 7 == 0:
                start += 1
            else:
                return False

        return True


s = Solution()
# s.validUtf8([237, 140, 4])
# s.validUtf8([235, 140, 4])
# s.validUtf8([197, 130, 1])
s.validUtf8([230, 100, 102, 231, 154, 132, 13, 10])
# s.validUtf8([237])
# s.validUtf8([250, 162, 138, 147, 240])
# utf_ = s.validUtf8([197, 130])
# print(utf_)
