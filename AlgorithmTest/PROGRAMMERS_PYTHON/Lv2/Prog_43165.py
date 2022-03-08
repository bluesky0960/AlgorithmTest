# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟넘버
from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])
    while q:
        num, idx = q.popleft()
        idx+=1
        if idx < len(numbers):
            q.append([num+numbers[idx], idx])
            q.append([num-numbers[idx], idx])
        else:
            if num==target:
                answer+=1
    return answer

def dfs(num, idx):
    if idx==n:
        if num == tar:
            answer+=1
        return
    else:
        dfs(num+numbers[idx], idx+1)
        dfs(num-numbers[idx], idx+1)
        