import collections
import sys


def solution(call):
    dict = collections.defaultdict(int)
    for good in call:
        dict[good.lower()] += 1
        dict[good.upper()] += 1

    m = -sys.maxsize
    for x in dict.items():
        m = max(m, x[1])

        if m == x[1]:
            call = call.replace(x[0], '')

    print(call)
    return call


solution("abcabcdefabc")
solution("abxdeydeabz")
solution("ABCabcA")
