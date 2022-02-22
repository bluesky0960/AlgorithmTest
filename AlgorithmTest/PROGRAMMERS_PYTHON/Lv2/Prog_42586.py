#https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for p, s in zip(progresses, speeds):
        if (100-p) % s == 0:
            q.append((100-p)//s)
        else:
            q.append((100-p)//s + 1)
            
    while q:
        cnt = 1
        start = q.popleft()
        while q and start >= q[0]:
            q.popleft()
            cnt+=1
        answer.append(cnt)
        
    return answer