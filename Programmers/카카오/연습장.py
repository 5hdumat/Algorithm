def km_match(txt, pat):
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

    pt = pp = 0
    while pt < len(txt) and pp < len(pat):
        print(txt[pt], pt, pat[pp], pp)
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    if pp == len(pat):
        return 1
    else:
        return 0

km_match('abcabcdefabc')