import sys


def solution(s):
    answer = sys.maxsize

    k = 1
    while k <= len(s) / 2:
        right = k
        characters = []

        for left in range(0, len(s), k):
            characters.append(s[left:right])
            right += k

        start = 0
        tmp = []
        count = 1
        for end in range(1, len(characters)):
            if characters[start] != characters[end]:
                if count > 1:
                    tmp.append(str(count) + characters[start])
                else:
                    tmp.append(characters[start])

                start = end
                count = 0

            count += 1
        else:
            if count > 1:
                tmp.append(str(count) + characters[start])
            else:
                tmp.append(characters[start])

        k += 1

        answer = min(answer, len(''.join(tmp)))

    print(answer)
    return answer


solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
