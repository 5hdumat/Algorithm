# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    output = {}
    for i in range(1, N+1):
        process_cnt = 0
        attempt_cnt = 0
        for stage in stages:
            if i <= stage:
                attempt_cnt += 1
                if i == stage:
                    process_cnt += 1
             
        if attempt_cnt == 0:
            output[i] = 0
        else:
            output[i] = (process_cnt / attempt_cnt)

    output = sorted(output.keys(), key=lambda x : output[x], reverse=True)
    # output는 dictionary이므로 sorted에 output을 그냥 넘기면 output의 keys가 들어갑니다. (keys는 생략이 가능합니다.)
    # 거기에 lambda는 기준을 output는[x]: 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력되게 됩니다.
 
    return output

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4, 4, 4, 4])


# 시간복잡도를 O(n) 으로 개선한 문제풀이
def solution(n, stages):
    accessed_cnts = [0 for _ in range(n+2)]
    stay_cnts = [0 for _ in range(n+2)]

    for num in stages:
        stay_cnts[num] += 1

    accessed_cnts[n] = stay_cnts[n+1] + stay_cnts[n]
    
    for i in range(n-1, 0, -1):
        accessed_cnts[i] = accessed_cnts[i+1] + stay_cnts[i]

    results = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if stay_cnts[i] == 0:
            results[i] = (i, 1)
            continue
        results[i] = (i, 1 - stay_cnts[i]/accessed_cnts[i])
        
    results = results[1:n+1]
    
    results.sort(key=lambda item: item[0])
    results.sort(key=lambda item: item[1])

    ans = []
    for i, r in results:
        ans.append(i)
    return ans

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])