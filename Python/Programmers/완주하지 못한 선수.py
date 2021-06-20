# https://programmers.co.kr/learn/courses/30/lessons/42576

# 효율성 테스트 실패 (시간 초과)
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
        
    return participant[0]

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

# 공집합 초기화 -> 마라톤 선수 key, value 입력 -> 도착한 순서대로 -1 -> 값이 가장 큰 선수이름 리턴
def solution(participant, completion):
    p_set = {}
    
    for i in participant:
        if i in p_set:
            p_set[i] += 1
        else:
            p_set[i] = 1
            
    for i in completion:
        if i in p_set:
            p_set[i] -= 1
  
    answer = max(p_set.keys(), key = lambda k: p_set[k]) # 가장 큰 value를 갖는 key찾기

    print(answer)

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

# 내장 함수 collections 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

# 해시 함수를 사용한 정석 문제 풀이
def solution(participant, completion):
    p_set = {}
    tmp_hash = 0
    
    for part in participant:
        part_hash = hash(part)
        
        p_set[part_hash] = part # 모든 마라토너의 이름을 해시값으로 딕셔너리에 저장 한 후
        tmp_hash += part_hash # 해시값을 tmp_hash에 합산해놓는다.
        
    for comp in completion:
        comp_hash = hash(comp)
        tmp_hash -= comp_hash
    
    answer = p_set[tmp_hash]
    
    return answer

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
