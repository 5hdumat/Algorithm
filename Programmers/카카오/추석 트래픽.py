import datetime


def solution(lines):
    combined = []

    for log in lines:
        logs = log.split(' ')
        date = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()

        # tuple 2번쨰 인자
        # 1: 시작
        # 2: 종료
        combined.append((date - float(logs[2][:-1]) + 0.001, 1))
        combined.append((date, -1))

    combined.sort(key=lambda key: key[0])

    answer = 0
    current = 0
    for i, e1 in enumerate(combined):
        throughput = current

        # 1초 단위안에서 몇개가 실행중인가? (시작점 + a)
        for e2 in combined[i:]:
            if e2[0] - e1[0] >= 1:
                break

            if e2[1] == 1:
                throughput += 1

        answer = max(answer, throughput)

        # 동일 시간대에 몇개가 처리중인가? (시작점)
        current += e1[1]

    return answer


solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
# solution([
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ])
