import collections


def solution(record):
    answer = []

    dq = collections.deque(record)
    table = {}

    while dq:
        info = dq.popleft().split()

        if info[0] == 'Enter':
            table[info[1]] = info[2]
            answer.append((info[1], "님이 들어왔습니다."))

        elif info[0] == 'Leave':
            answer.append((info[1], "님이 나갔습니다."))

        else:
            table[info[1]] = info[2]

    for index, log in enumerate(answer):
        answer[index] = table[log[0]] + log[1]
        
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
