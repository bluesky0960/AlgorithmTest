#https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
    else:
        div_num = s//n
        mod_num = s%n

        for _ in range(n):
            answer.append(div_num)
        for i in range(1, mod_num+1):
            answer[-i] += 1
            
    return answer