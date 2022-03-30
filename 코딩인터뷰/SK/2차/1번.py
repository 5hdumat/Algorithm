import sys


def solution(goods):
    answer = []

    for index, good in enumerate(goods):
        goods.pop(index)
        text = str(goods)

        lp = 0
        rp = 1
        limit = sys.maxsize
        inherence = []
        while rp <= len(good):
            word = good[lp:rp]

            if text.count(word) > 0:
                rp += 1

            else:
                if good[lp:rp] not in inherence:
                    if inherence and limit > len(word):
                        inherence.clear()

                    if len(word) <= limit:
                        inherence.append(word)

                    limit = min(limit, len(word))
                lp += 1

        if inherence:
            answer.append(' '.join(sorted(inherence)))
        else:
            answer.append("None")

        goods.insert(index, good)

    print(answer)
    return answer


solution(["pencil", "cilicon", "contrabase", "picturelist"])
solution(["abcdeabcd", "cdabe", "abce", "bcdeab"])
