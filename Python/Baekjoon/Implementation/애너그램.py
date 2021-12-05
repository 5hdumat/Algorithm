# https://www.acmicpc.net/problem/6996
'''
3
blather reblath
maryland landam
bizarre brazier
'''
n = int(input())

for _ in range(n):
    a, b = input().split()

    h = 0
    for x in a:
        h += hash(x)

    for x in b:
        h -= hash(x)

    if h == 0:
        print("%s & %s are anagrams." % (a, b))
    else:
        print("%s & %s are NOT anagrams." % (a, b))

