#https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

from collections import deque
def solution(priorities, location):
    answer = 0
    
    sort_list = sorted(priorities, reverse=True)
    
    p_list = [[i, 0] for i in priorities]
    p_list[location][1]=1
    
    q = deque(p_list)
    
    print(q)
    print(sort_list)
    
    cnt=0
    while q:
        start = q.popleft()
        if start[0] != sort_list[cnt]:
            q.append(start)
        else:
            cnt += 1
            if start[1] == 1:
                break
    answer = cnt
    return answer