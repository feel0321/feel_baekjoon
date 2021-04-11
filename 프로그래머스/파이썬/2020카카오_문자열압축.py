def check(s, dif):
    idx = 0
    count = 1
    answer = ''
    while idx <= len(s):
        idx += dif
        if s[idx - dif:idx] == s[idx:idx + dif]:
            count += 1
            continue
        if count > 1:
            answer += str(count) + s[idx - dif:idx]
            count = 1
            continue
        answer += s[idx - dif:idx]
    return len(answer)

def solution(s):
    answer = len(s)
    for idx in range(1, int(len(s) / 2) + 1):
        answer = min(answer, check(s, idx))
    return answer
'''
def check(s, dif):
    idx = 0
    count = 1
    answer = ''
    while idx <= len(s):
        idx += dif
        if s[idx - dif:idx] == s[idx:idx + dif]:
            count += 1
            continue
        answer += str(count) + s[idx - dif:idx]
        count = 1
    answer = answer.replace('1', '')
    #print('answer : ', answer)
    return len(answer)

def solution(s):
    answer = len(s)
    for idx in range(1, int(len(s) / 2) + 2):
        #print(idx)
        answer = min(answer, check(s, idx))
    return answer
=> 10ab 같은 상황을 고려하지 않아서 오답이다
'''
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))