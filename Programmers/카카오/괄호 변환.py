def is_balanced(p):
    checked = 0
    for _p in p:
        if _p == '(':
            checked += 1
        else:
            checked -= 1

        if checked == 0:
            return True

    return False


def is_right(p):
    checked = 0

    for _p in p:
        if _p == '(':
            checked += 1
        else:
            checked -= 1

        if checked < 0:
            return False

    return True


def solution(p):
    if is_right(p):
        return p

    for i, v in enumerate(p, 1):
        if i % 2 == 0:
            if is_balanced(p[:i]):
                u, v = p[:i], p[i:]
                break

    if is_right(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for cha in u[1:-1]:
            if cha == '(':
                answer += ')'
            else:
                answer += '('

        return answer

# print(solution("(()())()"))
# solution(")(")
print(solution("()))((()"))
# solution('')
