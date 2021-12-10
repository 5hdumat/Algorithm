# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    new_id = list(new_id.lower()) # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
  
    tmp_stack = []
    for i in range(0, len(new_id)):
        if new_id[i].isalpha() or new_id[i].isalnum() or new_id[i] in ['-', '_', '.']: # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.  
            tmp_stack.append(new_id[i])
    
    tmp = ''
    stack = []
    for i in range(0, len(tmp_stack)): 
        if tmp == '.' and tmp == tmp_stack[i]: # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
            continue
        else:
            stack.append(tmp_stack[i])
        
        tmp = tmp_stack[i]
        
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    while len(stack) != 0 and stack[0] == '.':
        stack.pop(0)
            
    while len(stack) != 0 and stack[-1] == '.':
        stack.pop()
            
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(stack) == 0:
        stack.append('a')
        
    elif len(stack) >= 16: # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        stack = stack[0:15]
        
        while stack[-1] == '.': # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
            stack.pop()
    
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(stack) <= 2:
            stack.append(stack[-1])
        
    answer = ''.join(stack)
    return answer
    
solution('...!@BaT#*..y.abcdefghijklm')

# 정규표현식을 이용한 문제풀이
import re
# [abck] : a or b or c or k
# [abc.^] : a or b or c or . or ^
# [a-d] : -와 함께 사용되면 해당 문자 사이의 범위에 속하는 문자 중 하나
# [0-9] : 모든 숫자
# [a-z] : 모든 소문자
# [A-Z] : 모든 대문자
# [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
# [^0-9] : ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매칭

def solution(new_id):
    st = new_id
    st = st.lower() # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    st = re.sub('[^a-z0-9\-_.]', '', st) # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    st = re.sub('\.+', '', st) # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    st = re.sub('^[.]|[.]$', '', st) # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    st = 'a' if len(st) == 0 else st[:15] # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    st = re.sub('^[.]|[.]$', '', st) # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    st = st if len(st) > 2 else st + ''.join([st[-1] for i in range(3-len(st))]) # # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    
    return st

solution('...!@BaT#*..y.abcdefghijklmm')