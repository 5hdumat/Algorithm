# https://www.acmicpc.net/problem/1786

def bm_match(txt, pat):
    global cnt, res

    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    while pt < len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    # print(skip)
    pt = pp = 0

    while pt < len(txt) and pp < len(pat):
        # print(pt, pp)
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

        if pp == len(pat):
            cnt += 1
            res.append(pt - pp + 1)
            pp = skip[pp]


txt = input()
pat = input()

cnt = 0
res = []
bm_match(txt, pat)

print(cnt)
print(*res)
